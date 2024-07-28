import streamlit as st
import pandas as pd
import pathlib
import os

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image(os.path.join(os.getcwd(),'images','photo2.JPG'))

with col2:
    st.title("Sanjay Dangwal")
    content = """Hi, I am Sanjay Dangwal! I am a Python programmer, and working in Tata Consultancy Services,
    I am Passionate and dedicated Python developer with a proven track record of delivering high-quality software 
    solutions. Proficient in developing web applications, APIs, and data processing scripts using Python and 
    associated frameworks. Skilled in both front-end and back-end development, I thrive in collaborative environments 
    and enjoy tackling complex challenges to deliver innovative solutions."""

    st.info(content)
content2 = """Below you can find some of the apps I have built in Python. Feel free to contact me!"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.2, 1.5])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df.iloc[0::2, ].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(str(pathlib.Path("images", row["image"])))
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df.iloc[1::2, ].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(str(pathlib.Path("images", row["image"])))
        st.write(f"[Source Code]({row['url']})")
