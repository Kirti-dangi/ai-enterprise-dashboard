import os
import pandas as pd
from groq import Groq

# 🔐 SECURE: API KEY FROM STREAMLIT / ENV (NOT HARD-CODED)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 📊 SAMPLE DATA
df = pd.DataFrame({
    "City": ["Delhi", "Mumbai", "Chennai", "Kolkata"],
    "Sales": [250, 400, 180, 300],
    "Profit": [50, 120, 30, 80]
})

def ai_response(query):

    prompt = f"""
You are a Business Intelligence AI Analyst.

Dataset:
{df.to_string(index=False)}

Question:
{query}

Rules:
- Use only dataset values
- Give numeric + insight answer
- Be concise and professional
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a BI analyst AI."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content