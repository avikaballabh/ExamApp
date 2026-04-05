import streamlit as st


if "user" not in st.session_state or st.session_state.user is None:
    st.switch_page("app.py")
    st.stop()
if "user" not in st.session_state or st.session_state.role != "teacher":
    st.warning("Login as teacher")
    st.stop()

if "user" not in st.session_state or st.session_state.role != "teacher":
    st.warning("Login as teacher")
    st.stop()

st.title("👨‍🏫 Teacher Dashboard")

st.page_link("pages/Create_Exam.py", label="➕ Create Exam")
st.page_link("pages/Azd_Questions.py", label="📝 Add Questions")
st.page_link("pages/View_Results.py", label="📊 View Results")
import streamlit as st

# 🔐 Protect page
if "user" not in st.session_state or st.session_state.user is None:
    st.switch_page("app.py")
    st.stop()

# 🚪 Logout button (TOP RIGHT STYLE)
col1, col2 = st.columns([8, 2])

with col2:
    if st.button("🚪 Logout"):
        st.session_state.user = None
        st.session_state.role = None
        st.switch_page("app.py")