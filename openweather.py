
import json, requests 

APIkey = "7b3f6e505b459240312ab53b78c72e8b"
location = 'london'

# http://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APIkey
st.text(url)

response = requests.get(url)  

weatherData = json.loads(response.text)

st.text (weatherData['main']['temp_max']) 
location = 'london'

# check API documentation to see what structure of URL is needed to access the data
# http://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APIkey
# print(url)


# Download the JSON data from OpenWeatherMap.org's API.
response = requests.get(url)  
# Uncomment to see the raw JSON text:
# print(response.text)  


# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Uncomment to see the raw JSON text:
# print(weatherData) 
# from pprint import pprint 
# pprint(weatherData) 

print(weatherData['main']['temp_max']) 
# more???????????
location = 'london'

#check API documentation to see what structure of URL is needed to access the data
#http://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APIkey
#print(url)


# Download the JSON data from OpenWeatherMap.org's API.
response = requests.get(url)  
# Uncomment to see the raw JSON text:
#print(response.text)  


#Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Uncomment to see the raw JSON text:
#print(weatherData) 
#from pprint import pprint 
#pprint(weatherData) 

print(weatherData['main']['temp_max']) 
