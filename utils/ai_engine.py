import pandas as pd
from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def find_column(df, keywords):
    for col in df.columns:
        for k in keywords:
            if k in col.lower():
                return col
    return None


def ai_response(query, df):

    if df is None or df.empty:
        return "Dataset not loaded"

    query = query.lower()

    try:

        # ---------------- AVG ----------------
        if "average" in query:

            col = find_column(df, ["sales", "sale", "amount", "revenue", "profit"])

            if col:
                return f"📊 Average {col}: {df[col].astype(float).mean():.2f}"

            return "❌ No suitable numeric column found for average"

        # ---------------- MAX ----------------
        if "max" in query or "highest" in query:

            col = find_column(df, ["sales", "sale", "amount", "revenue", "profit"])

            if col:
                return f"📈 Maximum {col}: {df[col].astype(float).max()}"

            return "❌ No suitable numeric column found"

        # ---------------- SUM ----------------
        if "total" in query:

            col = find_column(df, ["sales", "sale", "amount", "revenue", "profit"])

            if col:
                return f"💰 Total {col}: {df[col].astype(float).sum()}"

        # ---------------- FALLBACK AI ----------------
        completion = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a data analyst assistant."},
                {"role": "user", "content": f"Columns: {list(df.columns)} | Query: {query}"}
            ]
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"