import json,requests
from pprint import pprint

st.header("Datamuse")

keyword = st.text_input('plz give me a keyword ')

choice = st.selectbox("What you want to know? ", ("Synonyms", "Antonyms", "Sounds like", "Means like"))
if choice == "Synonyms":
  st.write("You selected synonyms of " + keyword)
  elif choice == "Antonyms" :
    st.write("You selected antonyms of " + keyword)
    elif choice == "Sounds like":
      st.write ("You selected sounds like of " + keyword)
      else choice == "Means like":
        st.write("You selected means like " + keyword)
  

url1= 'https://www.datamuse.com/api/words?rel_syn=' + keyword + '&max=10'
url2= 'https://www.datamuse.com/api/words?rel_ant=' + keyword + '&max=10'
url3= 'https://www.datamuse.com/api/words?sl=' + keyword + '&max=10'
url4= 'https://www.datamuse.com/api/words?ml' + keyword + '&max=10'


response1 = requests.get(url1)   
response2 = requests.get(url2)
response3 = requests.get(url3)   
response4 = requests.get(url4) 

dataFromDatamuse1 = json.loads(response1.text) 
dataFromDatamuse2 = json.loads(response2.text)
dataFromDatamuse3 = json.loads(response3.text)
dataFromDatamuse4 = json.loads(response4.text)
pprint(dataFromDatamuse1)
pprint(dataFromDatamuse2)

st.text("you give me the word ", keyword, ". Its synonym are as following: ")
for eachentry in dataFromDatamuse1:
  print("-", eachentry["word"])
for eachentry in dataFromDatamuse2:
  print("-", eachentry["word"])
for eachentry in dataFromDatamuse3:
  print("-", eachentry["word"])
foreachentry in dataFromDAtamuse4:
  print("-", eachentry ["word"]

