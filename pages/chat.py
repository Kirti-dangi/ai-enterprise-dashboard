import streamlit as st
from utils.ai_engine import ai_response

st.title("💬 AI Data Analyst Chat")

q = st.text_input("Ask about your data")

if q:
    st.success(ai_response(q))