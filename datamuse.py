import json,requests
from pprint import pprint

st.header("Datamuse")

keyword = st.text_input('plz give me a keyword ')

choice = st.selectbox("What you want to know? ", ("Synonyms", "Antonyms", "Sounds like", "Means like"))
if choice == "Synonyms":
  st.write("You selected synonyms of " + keyword)
if choice == "Antonyms" :
  st.write("You selected antonyms of " + keyword)
if choice == "Sounds like":
  st.write ("You selected sounds like of " + keyword)
if choice ==("You selected synonyms of " + keyword)
  st.write("You selected means like " + keyword)

