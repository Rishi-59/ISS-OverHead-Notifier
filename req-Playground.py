import requests
import curlify
import pprint

response = requests.get(url="http://api.open-notify.org/iss-now.json")

print(response.raise_for_status())
print(curlify.to_curl(response.request))
print(response.request)
print(response.status_code)
pprint.pprint(response.json())

data = response.json()
latitude = data['iss_position']['latitude']
longitude = data['iss_position']['longitude']
iss_position = (latitude, longitude)
print(iss_position)
print(f"The ISS is currently at latitude {latitude} and longitude {longitude}.")