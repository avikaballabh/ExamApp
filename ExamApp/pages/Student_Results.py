import streamlit as st

if "user" not in st.session_state or st.session_state.user is None:
    st.switch_page("app.py")
    st.stop()
if "user" not in st.session_state :
    st.warning("Access denied. Login to view results.")
    st.stop()
import pandas as pd
from db import *

st.title("My Results")

data = c.execute("SELECT * FROM results WHERE username=?",
                 (st.session_state.user,)).fetchall()

if data:
    df = pd.DataFrame(data, columns=["User", "Exam", "Score"])
    st.dataframe(df)
    st.write("Attempts:", len(df))

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