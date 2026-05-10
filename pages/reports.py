import streamlit as st
from utils.data_loader import load_data

st.title("📑 Reports")

df = load_data()

st.write("### Dataset")
st.dataframe(df)

st.download_button(
    "Download CSV",
    df.to_csv(index=False),
    "report.csv"
)