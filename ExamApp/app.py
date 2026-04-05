import streamlit as st
from db import *


init_db()
if "user" not in st.session_state:
    st.session_state.user = None
    st.session_state.role = None

# 🚫 BLOCK ACCESS BEFORE LOGIN
if st.session_state.user is None:
    st.title("🔐 Login Required")

    menu = ["Login", "Register"]
    choice = st.selectbox("Menu", menu)

    if choice == "Register":
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")
        role = st.selectbox("Role", ["student", "teacher"])

        if st.button("Create Account"):
            try:
                c.execute("INSERT INTO users VALUES (?, ?, ?)", (user, pwd, role))
                conn.commit()
                st.success("Account created!")
            except:
                st.error("User exists")

    if choice == "Login":
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")

        if st.button("Login"):
            res = c.execute(
                "SELECT * FROM users WHERE username=? AND password=?",
                (user, pwd)
            ).fetchone()

            if res:
                st.session_state.user = res[0]
                st.session_state.role = res[2]
                st.success("Logged in!")
                st.rerun()
            else:
                st.error("Invalid credentials")

    st.stop()  # ⛔ STOP APP HERE if not logged in

st.title("📚 Exam Portal")

if "user" not in st.session_state:
    st.session_state.user = None
    st.session_state.role = None

menu = ["Login", "Register"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Register":
    st.subheader("Register")

    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    role = st.selectbox("Role", ["student", "teacher"])

    if st.button("Create Account"):
        try:
            c.execute("INSERT INTO users VALUES (?, ?, ?)", (user, pwd, role))
            conn.commit()
            st.success("Account created!")
        except:
            st.error("User already exists")

if choice == "Login":
    st.subheader("Login")

    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        res = c.execute("SELECT * FROM users WHERE username=? AND password=?",
                        (user, pwd)).fetchone()

        if res:
            st.session_state.user = res[0]
            st.session_state.role = res[2]
            st.success("Logged in!")

            if res[2] == "teacher":
                st.switch_page("pages/Teacher_Dashboard.py")
            else:
                st.switch_page("pages/Student_Dashboard.py")
        else:
            st.error("Invalid credentials")
if st.session_state.role == "teacher":
        st.switch_page("pages/Teacher_Dashboard.py")

elif st.session_state.role == "student":
        st.switch_page("pages/Student_Dashboard.py")