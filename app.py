import streamlit as st
from utils.auth import login_user, register_user

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI SaaS Analytics Platform",
    page_icon="📊",
    layout="wide"
)

# ---------------- LIGHT THEME UI ----------------
st.markdown("""
<style>
body {
    background-color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "auth" not in st.session_state:
    st.session_state.auth = False

# ---------------- LOGIN PAGE ----------------
if not st.session_state.auth:

    st.title("🚀 AI SaaS Analytics Platform")
    st.subheader("Login to access your dashboard")

    tab1, tab2 = st.tabs(["Login", "Register"])

    # ---------- LOGIN ----------
    with tab1:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if login_user(username, password):
                st.session_state.auth = True
                st.session_state.user = username
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid credentials")

    # ---------- REGISTER ----------
    with tab2:
        new_user = st.text_input("New Username")
        new_pass = st.text_input("New Password", type="password")

        if st.button("Register"):
            if register_user(new_user, new_pass):
                st.success("User created successfully! Now login.")
            else:
                st.error("User already exists")

    st.stop()

# ---------------- MAIN APP ----------------
st.sidebar.title("📌 Navigation")
st.sidebar.success(f"Logged in as: {st.session_state.user}")

st.sidebar.info("""
Pages:
- Dashboard
- Chat (AI Analyst)
- Reports
""")

st.title("📊 AI SaaS Analytics System")
st.write("Welcome to your enterprise AI dashboard 🚀")

st.markdown("---")

st.success("✅ System is running successfully")

st.info("Use the left sidebar to navigate between pages")