import streamlit as st
from database import validate_user

#st.set_page_config(page_title="Wellness Hub Login", layout="wide", page_icon="🧑‍⚕️")
# Check if the page parameter is set to login
query_params = st.experimental_get_query_params()
if query_params.get("page") == ["login"]:
    st.title("Login Page")
    page_bg_img = '''
    <style>
    body {
    background-color: black;
    background-size: cover;
    }
    </style>
    '''

    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if validate_user(email, password):
            st.session_state["logged_in"] = True
            st.success("Login successful!")
            st.experimental_set_query_params(page="app")  # Clear the query parameter
            st.experimental_rerun()  # Redirect to app.py
        else:
            st.error("Invalid email or password!")