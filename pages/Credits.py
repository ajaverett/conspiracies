"""
Credit page for team members.
"""
import streamlit as st

container = st.container()

with st.container():
    st.title('Credits')
    st.subheader('_Team Lead_')
    st.write('Aj Averett - Data Science Major')
    st.subheader('_Members_')
    st.write('Kaden Mills - Computer Science Major')
    st.write('Linda Spellman - Computer Science Major')
    st.write('Tyler Aston - Software Engineering Major')

    st.markdown('<br><br><br>',unsafe_allow_html=True)

#Balloons
    clicked = st.button('Click here to see balloons!')
    if clicked:
        st.balloons()
