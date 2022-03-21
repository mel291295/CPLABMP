import streamlit as st
import json, requests 

st.header("OpenWeather")

APIkey = "7b3f6e505b459240312ab53b78c72e8b"
location= st.text_input("Gimmi a city", "london")

url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APIkey + '&units=metric'
print(url)

city = st.radio("Gimmi a location",('London', 'Roma', 'Munich'))
if city == 'London':
     st.write('You selected London.')
 else:
     st.write("You didn't select London.")


