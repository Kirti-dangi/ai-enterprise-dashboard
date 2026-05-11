import streamlit as st
import pandas as pd

st.title("📑 Reports & Data Upload")

# ---------------- UPLOAD SECTION ----------------
uploaded_file = st.file_uploader("Upload Dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("Dataset uploaded successfully!")

    # Save for other pages (AI chat can use it)
    st.session_state["df"] = df

    st.subheader("📄 Data Preview")
    st.dataframe(df)

    st.subheader("📊 Summary Statistics")
    st.write(df.describe())

    # ---------------- REPORTS SECTION ----------------
    st.subheader("📈 Generated Insights")

    st.write(f"Total Rows: {df.shape[0]}")
    st.write(f"Total Columns: {df.shape[1]}")

    numeric_cols = df.select_dtypes(include=['number']).columns

    if len(numeric_cols) > 0:
        st.write("### Column Averages")
        st.write(df[numeric_cols].mean())

else:
    st.info("Please upload a dataset to generate reports")