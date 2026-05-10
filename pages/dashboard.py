import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

st.title("📊 Dashboard")

df = load_data()

fig = px.bar(df, x="City", y="Sales", title="Sales by City")
st.plotly_chart(fig)

fig2 = px.pie(df, names="City", values="Profit", title="Profit Distribution")
st.plotly_chart(fig2)