import json,requests
from pprint import pprint


keyword=input('plz give me a keyword ')
url1= 'https://www.datamuse.com/api/words?rel_syn=' + keyword + '&max=10'
url2= 'https://www.datamuse.com/api/words?rel_ant=' + keyword + '&max=10'

response1 = requests.get(url1)   
response2 = requests.get(url2) 

dataFromDatamuse1 = json.loads(response1.text) 
dataFromDatamuse2 = json.loads(response2.text) 
pprint(dataFromDatamuse1)
pprint(dataFromDatamuse2)

print("you give me the word ", keyword, ". Its synonym are as following: ")
for eachentry in dataFromDatamuse1:
  print("-", eachentry["word"])
for eachentry in dataFromDatamuse2:
  print("-", eachentry["word"])
