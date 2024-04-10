#source used as skeleton: https://stackabuse.com/how-to-get-json-from-a-url-in-python/
#https://www.youtube.com/watch?v=bHCHKeJ6bI8

import requests
import json

#Sends a GET request to the URL
response = requests.get('https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en')

#Parses the response as JSON
data = response.json()
#Sends the file to the same folder I keep the code. This would not work until I used the 'r' to convert the line. Source used: https://www.digitalocean.com/community/tutorials/python-raw-string

file_path = r"C:\Users\darac\OneDrive\Desktop\WSAA-Coursework\assignments\data.json"

#Creates new file
with open(file_path, "w") as json_file:
    #Write the JSON data to the file
    #source used: https://ioflood.com/blog/python-write-json-to-file/ 
    json.dump(data, json_file)

