import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input(label="Your Email Address", key="user_email")
    row_message = st.text_area(label="Your Message")
    message = f"""\
Subject: Email from Portfolio App

From: {user_email}
{row_message}
"""
    submit_button = st.form_submit_button(label="Submit")
    if submit_button:
        print("Submit button pressed.")
        send_email(message)
        st.info("Your message has been sent successfully.")

