import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Dashboard - Upload Dataset")

# ✅ ALWAYS SHOW UPLOAD OPTION
uploaded_file = st.file_uploader("📂 Upload CSV Dataset", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # SAVE GLOBALLY FOR OTHER PAGES
    st.session_state["df"] = df

    st.success("Dataset uploaded successfully!")

    st.subheader("📌 Preview")
    st.dataframe(df.head())

    # CLEAN COLUMN NAMES
    df.columns = df.columns.str.lower()

    # AUTO CHARTS
    num_cols = df.select_dtypes(include="number").columns

    if len(num_cols) == 0:
        st.warning("No numeric columns found")
    else:
        for col in num_cols:
            st.subheader(f"📊 {col} Distribution")
            fig = px.histogram(df, x=col)
            st.plotly_chart(fig, use_container_width=True)