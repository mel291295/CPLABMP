import streamlit as st
st.header("hello world")  
st.text("from Brixen")  
title = st.text_input('Gimme a movie title', 'lorem ipsum')
st.write('The current movie title is', title)

genre = st.radio("What's your favorite movie genre", help=None, ('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
     st.write('You selected comedy.')
else:
     st.write("You didn't select comedy.")
