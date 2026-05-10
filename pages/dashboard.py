import streamlit as st
import pandas as pd
import plotly.express as px

st.markdown("## 📊 Executive Dashboard")
st.markdown("---")

file = st.file_uploader("Upload CSV")

if file:
    df = pd.read_csv(file)

    st.dataframe(df)

    num = df.select_dtypes(include="number").columns
    cat = df.select_dtypes(exclude="number").columns

    y = num[0]
    x = cat[0] if len(cat)>0 else df.columns[0]

    c1, c2, c3 = st.columns(3)

    c1.metric("Rows", len(df))
    c2.metric("Max", df[y].max())
    c3.metric("Avg", round(df[y].mean(),2))

    chart = st.selectbox("Chart Type", ["Bar","Line","Pie"])

    if chart == "Bar":
        st.plotly_chart(px.bar(df, x=x, y=y), use_container_width=True)

    if chart == "Line":
        st.plotly_chart(px.line(df, x=x, y=y), use_container_width=True)

    if chart == "Pie":
        st.plotly_chart(px.pie(df, names=x, values=y), use_container_width=True)