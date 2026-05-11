import streamlit as st
import pandas as pd
from utils.ai_engine import ai_response

st.title("📊 AI SaaS Analytics Dashboard")

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Dataset Loaded Successfully!")

    st.subheader("📄 Preview")
    st.dataframe(df)

    st.subheader("📊 Summary")
    st.write(df.describe())

    # Store dataframe in session for AI chat
    st.session_state["df"] = df

else:
    st.info("Upload a dataset to enable AI analysis")