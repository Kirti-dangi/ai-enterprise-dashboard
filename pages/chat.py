import streamlit as st
import pandas as pd

st.markdown("## 🤖 AI Data Analyst")
st.markdown("---")

file = st.file_uploader("Upload CSV")

if file:
    df = pd.read_csv(file)

    col = df.select_dtypes(include="number").columns[0]

    q = st.text_input("Ask AI (max / min / top / summary)")

    if q:
        q = q.lower()

        if "max" in q:
            st.dataframe(df[df[col]==df[col].max()])

        elif "min" in q:
            st.dataframe(df[df[col]==df[col].min()])

        elif "top" in q:
            st.dataframe(df.sort_values(col, ascending=False).head(5))

        elif "summary" in q:
            st.write(df.describe())

        else:
            st.info("Try: max, min, top, summary")