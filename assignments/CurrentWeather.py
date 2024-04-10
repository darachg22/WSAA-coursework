#Using the URL below
#https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m
#Write a python program called currentweather.py that will print out the current temperature on the console (and only the temperature)
#I have set the lat/long to my location, you may use that or a different location.

#Source code used: import requests # API URL API_URL = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m" # HTTP request response = requests.get(API_URL) # Getting data in JSON format data = response.json() # Getting the current temperature current_temperature = data["current"]["temperature_2m"] # Printing the current temperature print(f"Current temperature: {current_temperature} °C")
#I shortened this code to only print the temperature.

#Import requests which sends http requests. 
import requests

#URL
URL = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m"

#HTTP request which gets the information from the API found in the URL. 
response = requests.get(URL)

#Changes the response to JSON format
data = response.json()

#Gets the current temperature
current_temperature = data["current"]["temperature_2m"]

#Prints the current temperature
print(f"Current temperature: {current_temperature} °C")
