import streamlit as st
st.header("hello world")  
st.text("from Brixen")  

title = st.text_input('Gimme a movie title', '<enter a movie title here in English>', max_chars= 7)
st.write('The current movie title is', title)
