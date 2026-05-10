import streamlit as st
from utils.auth import login_user, register_user

st.set_page_config(page_title="AI SaaS Platform", layout="wide")

st.title("🚀 AI SaaS Analytics Platform")

if "auth" not in st.session_state:
    st.session_state.auth = False

# ---------------- LOGIN ----------------
if not st.session_state.auth:

    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")

        if st.button("Login"):
            if login_user(user, pwd):
                st.session_state.auth = True
                st.session_state.user = user
                st.rerun()
            else:
                st.error("Invalid credentials")

    with tab2:
        nu = st.text_input("New Username")
        np = st.text_input("New Password", type="password")

        if st.button("Register"):
            register_user(nu, np)
            st.success("Account created")

    st.stop()

# ---------------- MAIN APP ----------------
st.sidebar.success(f"Logged in as {st.session_state.user}")

st.sidebar.title("Navigation")
st.sidebar.info("Go to Dashboard / Chat / Reports pages")