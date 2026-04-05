import streamlit as st

if "user" not in st.session_state or st.session_state.user is None:
    st.switch_page("app.py")
    st.stop()
if "user" not in st.session_state or st.session_state.role != "student":
    st.warning("Access denied. Login as student.")
    st.stop()
st.title("Student Dashboard")

st.page_link("pages/Attempt_Exam.py", label="📝 Attempt Exam")
st.page_link("pages/Student_Results.py", label="📈 My Results")


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