import json
import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
if response.status_code != 200:
    print("Error connecting to the API")
    print("Error: {0}".append(str(response.status_code)))
else:
    data =response.json()
    print(data)
    latitude = data["iss_position"]["latitude"]



    print("ISS is currently located at:")
    print(f"latitude: {latitude}")
    print(f"Longitude: " + str(data["iss_position"]["longitude"]))
    print("Message: " + str(data["message"]))
    print("Timestamp: " + str(data["timestamp"]))

