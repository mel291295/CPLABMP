import streamlit as st

keyword = st.text_input('plz give me a keyword: ', "word")

choice = st.selectbox(
  "What you want to know? ",
  ("Synonyms", "Antonyms", "Sounds like", "Means like"))

st.write("Your selected: " choice)

if choice == "Synonyms":
  url= 'https://www.datamuse.com/api/words?rel_syn=' + keyword + '&max=10'
  elif choice == "Antonyms" :
    url= 'https://www.datamuse.com/api/words?rel_ant=' + keyword + '&max=10'
    elif choice == "Sounds like":
      url= 'https://www.datamuse.com/api/words?sl=' + keyword + '&max=10'
      else choice == "Means like":
        url= 'https://www.datamuse.com/api/words?ml=' + keyword + '&max=10'
  

response = requests.get(url)   

dataFromDatamuse = json.loads(response.text) 

st.write(dataFromDatamuse)


st.text("you give me the word ", keyword, ". The results are: ")
for eachentry in dataFromDatamuse:
  print("-", eachentry["word"])


