import streamlit as st
from utils.ai_engine import ai_response

st.title("💬 AI Data Analyst Chat")

user_input = st.text_input("Ask about your data")

df = st.session_state.get("df", None)

if user_input:
    response = ai_response(user_input, df)
    st.write(response)