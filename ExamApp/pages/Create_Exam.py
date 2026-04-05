
import streamlit as st

if "user" not in st.session_state or st.session_state.user is None:
    st.switch_page("app.py")
    st.stop()
if "user" not in st.session_state or st.session_state.role != "teacher":
    st.warning("Login as teacher")
    st.stop()
from db import *

st.title("Create Exam")

title = st.text_input("Exam Title")

if st.button("Create"):
    c.execute("INSERT INTO exams (teacher, title) VALUES (?, ?)",
              (st.session_state.user, title))
    conn.commit()
    st.success("Exam Created!")
    


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