import streamlit as st

st.set_page_config(page_title="AI SaaS Platform", layout="wide")

# ---------- CLEAN UI ----------
st.markdown("""
<style>
.stApp {
    background-color: #f7f9fc;
}
section[data-testid="stSidebar"] {
    background-color: #0f172a;
}
section[data-testid="stSidebar"] * {
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.title("🚀 AI SaaS Analytics Platform")
st.markdown("### PowerBI + ChatGPT Style Dashboard")

st.success("System is running successfully")

# ---------- SIDEBAR ----------
st.sidebar.title("📊 Navigation Panel")

st.sidebar.markdown("""
👉 Dashboard  
👉 AI Chat  
👉 Reports  
""")

st.sidebar.info("Select pages from below menu")