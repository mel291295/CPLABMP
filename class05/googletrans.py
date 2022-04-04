
from googletrans import Translator
import streamlit as st

translator = Translator() 

word= st.text_input("Give me a word: ", "") 
if word !="":
  abc = translator.translate (word, dest= "it")
  st.write ("The translation is ", abc.text) 
