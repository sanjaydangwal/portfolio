import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo1.jpg')

with col2:
    st.title("Sanjay Dangwal")
    content = """Hi, I am Sanjay Dangwal! I am a Python programmer, and working in Tata Consultancy Services,
    I am Passionate and dedicated Python developer with a proven track record of delivering high-quality software 
    solutions. Proficient in developing web applications, APIs, and data processing scripts using Python and 
    associated frameworks. Skilled in both front-end and back-end development, I thrive in collaborative environments 
    and enjoy tackling complex challenges to deliver innovative solutions."""

    st.info(content)
