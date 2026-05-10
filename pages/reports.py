import streamlit as st
import pandas as pd
from fpdf import FPDF

st.markdown("## 📄 Report Generator")
st.markdown("---")

file = st.file_uploader("Upload CSV")

if file:
    df = pd.read_csv(file)

    st.dataframe(df)

    if st.button("Generate PDF"):

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 12)

        pdf.cell(200,10,"Enterprise SaaS Report",ln=True)
        pdf.cell(200,10,f"Rows: {len(df)}",ln=True)
        pdf.cell(200,10,str(df.describe()),ln=True)

        pdf.output("report.pdf")

        st.download_button("Download Report", open("report.pdf","rb"))