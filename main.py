import langchain_helper as lch
import streamlit as st

st.title("Username Generator")

user_platform = st.sidebar.selectbox("Select Platform",("Github","Twitter","Reddit","Instagram","Facebook","X","YouTube"))

user_color = st.sidebar.text_area("Wanna add a color?",max_chars=15)

user_keyword = st.sidebar.text_area("Any other keyword?",max_chars=15)

response = lch.generate_username(user_platform,user_color,user_keyword)

st.text(response['usernames'])