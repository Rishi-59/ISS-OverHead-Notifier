import requests
import pprint
import datetime as dt

MY_LAT = 18.508921
MY_LNG = 73.926025

parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LNG,
    "formatted" : 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
print("\n\n\n\n*************************************************\n\n")
pprint.pprint(response.json())
print("\n\n*************************************************\n\n\n\n")

data = response.json()
data = data["results"]
time = data["sunrise"].split("T")[1].split(":")[0]
sun_rise = int(time)
time = data["sunset"].split("T")[1].split(":")[0]
sun_set = int(time)

print(sun_rise , sun_set)

time_now = dt.datetime.now(dt.timezone.utc)
current_hour = int(time_now.hour)
print(current_hour)
if sun_rise < current_hour or current_hour < sun_set :
    print("ayyyy")