from googletrans import Translator

translator = Translator()
while True: 
  word= st.text_input("Give me a word: ", word) 
  if word == "nothing":
    st.text("ok bye! ")
    break
  destlang= st.text_input("des lang like es or es: ")
  abc = translator.translate(word, dest=destlang)
  st.text("The translation is ", abc.text) 
