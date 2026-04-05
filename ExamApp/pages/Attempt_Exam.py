import streamlit as st
import streamlit as st


if "user" not in st.session_state or st.session_state.user is None:
    st.switch_page("app.py")
    st.stop()
if "user" not in st.session_state or st.session_state.role != "student":
    st.warning("Access denied. Login as student.")
    st.stop()
from db import *

st.title("Attempt Exam")

exams = c.execute("SELECT * FROM exams").fetchall()
exam_dict = {e[2]: e[0] for e in exams}

exam_name = st.selectbox("Select Exam", list(exam_dict.keys()))
exam_id = exam_dict[exam_name]

questions = c.execute("SELECT * FROM questions WHERE exam_id=?",
                      (exam_id,)).fetchall()

answers = {}
score = 0

for q in questions:
    st.write(q[2])
    if q[3] == "MCQ":
        ans = st.radio("Choose", [q[4], q[5], q[6], q[7]], key=q[0])
    else:
        ans = st.text_input("Answer", key=q[0])
    answers[q[0]] = ans

if st.button("Submit"):
    for q in questions:
        if answers[q[0]] == q[8]:
            score += 1

    c.execute("INSERT INTO results VALUES (?, ?, ?)",
              (st.session_state.user, exam_id, score))
    conn.commit()

    st.success(f"Score: {score}/{len(questions)}")
    

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