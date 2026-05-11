import streamlit as st
import pandas as pd

st.title("📑 Reports")

# -----------------------------
# STEP 1: Get dataset
# -----------------------------
df = st.session_state.get("df")

# -----------------------------
# STEP 2: If no dataset, show upload option
# -----------------------------
if df is None:
    st.warning("No dataset found. Please upload a CSV file.")

    uploaded_file = st.file_uploader("📂 Upload Dataset for Reports", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state["df"] = df
        st.success("Dataset loaded successfully!")

# -----------------------------
# STEP 3: If dataset exists, show report
# -----------------------------
if df is not None:

    st.subheader("📊 Dataset Summary")
    st.write(df.describe())

    st.subheader("📌 Column Info")
    st.write(df.dtypes)

    st.subheader("📈 Insights")

    numeric_cols = df.select_dtypes(include="number").columns

    for col in numeric_cols:
        st.write(f"✔ {col}")
        st.write(f"   - Total: {df[col].sum()}")
        st.write(f"   - Average: {df[col].mean()}")
        st.write(f"   - Max: {df[col].max()}")