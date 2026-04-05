import streamlit as st

if "user" not in st.session_state or st.session_state.user is None:
    st.switch_page("app.py")
    st.stop()

import pandas as pd
from db import *

st.title("Results")

exams = c.execute("SELECT * FROM exams WHERE teacher=?",
                  (st.session_state.user,)).fetchall()

for exam in exams:
    st.subheader(exam[2])
    data = c.execute("SELECT * FROM results WHERE exam_id=?",
                     (exam[0],)).fetchall()

    if data:
        df = pd.DataFrame(data, columns=["User", "Exam", "Score"])
        st.dataframe(df)
        st.write("Attempts:", len(df))
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