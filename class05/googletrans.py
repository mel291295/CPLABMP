from googletrans import Translator

translator = Translator()
while True: 
  word= input ("Gimme a word to translate: ") 
  if word == "nothing":
    print("ok bye! ")
    break
  destlang= input("des lang like es or es: ")
  abc = translator.translate(word, dest=destlang)
  print("The translation is ", abc.text) 
