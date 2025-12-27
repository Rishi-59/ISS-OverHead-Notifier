import requests
import datetime as dt
import smtplib
import time
import pprint

MY_LAT = 18.508921
MY_LNG = 73.926025

ISS_LOC_API  = "http://api.open-notify.org/iss-now.json"
SUN_API = "https://api.sunrise-sunset.org/json"

my_email = "kunalpmore.5959@gmail.com"
password = ""
recipient_email = "rishipmore.1144@gmail.com"

def make_request(url,params=None):
    response = requests.get(url=url , params=params)
    response.raise_for_status()
    return response.json()

def get_iss_location():
    iss_loc_response = make_request(ISS_LOC_API)
    return float(iss_loc_response['iss_position']['latitude']), float(iss_loc_response['iss_position']['longitude'])

def get_sun_times():
    parameters = {
        "lat" : MY_LAT,
        "lng" : MY_LNG,
        "formatted" : 0
    }
    sun_response = make_request(SUN_API,params=parameters)
    sun_data = sun_response["results"]
    sunrise_hour = int(sun_data["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(sun_data["sunset"].split("T")[1].split(":")[0])
    return sunrise_hour, sunset_hour

def is_iss_overhead(lat , lng):
    return (MY_LAT-5) <= lat <= (MY_LAT+5) and (MY_LNG-5) <= lng <= (MY_LNG+5)

def is_night(sunrise_hour, sunset_hour):
    current_hour = int(dt.datetime.now(dt.timezone.utc).hour)
    return current_hour >= sunset_hour or current_hour <= sunrise_hour

def send_email():
    with smtplib.SMTP("smtp.gmail.com" , 587 , timeout=30) as con :
        con.starttls()
        con.login(user=my_email , password=password)
        con.sendmail(from_addr=my_email,
                     to_addrs=recipient_email,
                     msg="Subject : ISS is close And also Night Look Up\n\n" \
                     "Hey Look Up ISS is above you in the sky")

while True:
    iss_latitude, iss_longitude = get_iss_location()
    sunrise_hour, sunset_hour = get_sun_times()
    if is_iss_overhead(iss_latitude, iss_longitude) and is_night(sunrise_hour, sunset_hour):
        send_email()
        time.sleep(10)
    else:
        print("ISS not overhead or it's not night time.")
        time.sleep(60)
    
    