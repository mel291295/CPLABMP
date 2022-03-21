import streamlit as st
import json, requests 

st.header("OpenWeather")

APIkey = "7b3f6e505b459240312ab53b78c72e8b"
location= st.text_input("Gimmi a city", "london")


#check API documentation to see what structure of URL is needed to access the data
#http://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APIkey + '&units=metric'
st.text(url)


# Download the JSON data from OpenWeatherMap.org's API.
response = requests.get(url)  
# Uncomment to see the raw JSON text:
st.text(response.text)  

#Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Uncomment to see the raw JSON text:
st.text(weatherData) 
#from pprint import pprint 

maxtemp = weatherData["main"]["temp_max"]
pprint(weatherData)  


