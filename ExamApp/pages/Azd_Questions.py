import streamlit as st

if "user" not in st.session_state or st.session_state.user is None:
    st.switch_page("app.py")
    st.stop()
if "user" not in st.session_state or st.session_state.role != "teacher":
    st.warning("Login as teacher")
    st.stop()
from db import *

st.title("Add Questions")

exams = c.execute("SELECT * FROM exams WHERE teacher=?",
                  (st.session_state.user,)).fetchall()

exam_dict = {e[2]: e[0] for e in exams}

exam_name = st.selectbox("Select Exam", list(exam_dict.keys()))
exam_id = exam_dict[exam_name]

q_type = st.selectbox("Type", ["MCQ", "Subjective"])
question = st.text_area("Question")

if q_type == "MCQ":
    o1 = st.text_input("Option 1")
    o2 = st.text_input("Option 2")
    o3 = st.text_input("Option 3")
    o4 = st.text_input("Option 4")
    ans = st.selectbox("Answer", [o1, o2, o3, o4])
else:
    o1 = o2 = o3 = o4 = ""
    ans = st.text_input("Answer")

if st.button("Add"):
    c.execute("""INSERT INTO questions
        (exam_id, question, q_type, option1, option2, option3, option4, answer)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (exam_id, question, q_type, o1, o2, o3, o4, ans))

    conn.commit()
    st.success("Added")
    

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