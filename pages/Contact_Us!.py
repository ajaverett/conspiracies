"""
A test contact form.
"""

import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px

container = st.container()

with container:
    container.header(f':blue[Thoughts?]')
    st.title('Give Us Feedback!')

    
contact_form = """
	<form action="https://formsubmit.co/lindaspellman@live.com" method="POST">
        <table>
        <input type="hidden" name="_captcha" value="false">
        <br>
        <br>
        <input type="text" name="Name" placeholder="Your name" required>
        <br>
        <br>
        <input type="email" name="Email" placeholder="Your email" required>
        <br>
        <br>
        <textarea name="Suggestion" placeholder="Feature Suggestion"></textarea>
        <br>
        <button type="submit">Send</button>
        </table
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# CSS call below not working as expected, based on tutorial video
# Use local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>/{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# --------------------------------

# # Using the "with" syntax
# with st.form(key='my_form'):
# 	text_input = st.text_input(label='Send us your feature suggestions!')
# 	submit_button = st.form_submit_button(label='Submit')

# if submit_button:
    
# --------------------------------

# form = st.form(key='my-form', clear_on_submit=True)
# name = form.text_input("Please enter your full name:")
# email = form.text_input("Please enter your email:")
# suggestions = form.text_input('Send us your feature suggestions!')
# submit = form.form_submit_button('Humorous Submit Button')

# if submit:
#     st.write(f"Thank you for your suggestion! We'll receive it shortly!")

