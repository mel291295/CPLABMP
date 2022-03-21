import streamlit as st
import json, requests 

st.header("OpenWeather")

APIkey = "7b3f6e505b459240312ab53b78c72e8b"
location= st.text_input("Gimmi a city", "london")

url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APIkey + '&units=metric'
print(url)
response = requests.get(url) 
weatherData = json.loads(response.text)

st.header(location+ " weather forecast")
st.write("the max tempo in ", location, "is" (weatherData['main']['temp_max']))

location = st.radio("How is the weather in",('London', 'Rome', 'Munich'))
if location == 'London':
     st.write('The weather in" location "is" weatherData)
else:
     st.write("The weather in " location "is" weatherData)
