# Update the signup.py file
import streamlit as st
from database import create_table, insert_user
#st.set_page_config(page_title="Wellness Hub", layout="wide", page_icon="🧑‍⚕️")
# Create the users table if it doesn't exist
create_table()

st.title("Signup Page")

email = st.text_input("Email")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

if st.button("Signup"):
    if password == confirm_password:
        if insert_user(email, password):
            st.success("Signup successful! Please log in.")
            if st.button("Go to Login"):
                st.experimental_set_query_params(page="login")
                st.experimental_rerun()  # Redirect to login page
        else:
            st.error("Email already exists!")
    else:
        st.error("Passwords do not match!")