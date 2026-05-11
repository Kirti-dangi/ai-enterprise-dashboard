import streamlit as st
from utils.ai_engine import ai_response

st.title("💬 AI Chat Analyst")

df = st.session_state.get("df")

if df is None:
    st.warning("⚠ Please upload dataset in Dashboard first")
    st.stop()

user_input = st.text_input("Ask your question")

if user_input:
    response = ai_response(user_input, df)
    st.write(response)