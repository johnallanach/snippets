# explanation of fields in API response: 
# https://openweathermap.org/api/one-call-api

import requests
import json 
import datetime

# complete url address 
complete_url =  "https://api.openweathermap.org/data/2.5/onecall"\
                "?lat=43.5501&lon=-80.2497&appid="\
                "a5ca3329d3bde61767dd81690b641cd2"

# get method of requests module 
# return response object 
response = requests.get(complete_url) 

# write response to text file for checking
with open("response.txt", "w") as writefile:
    writefile.write(str(response.text))

# json method of response object 
# convert json format data into 
# python format data
data = response.json()

# get current and forecasted weather data
current_weather = data["current"]
daily_forecast = data["daily"]
today_forecast = daily_forecast[0]
tomorrow_forecast = daily_forecast[1]

# get temps
current_temp = current_weather["temp"]-273.15
current_feelslike = current_weather["feels_like"]-273.15
today_temp = today_forecast["temp"]
today_temp_min = today_temp["min"]-273.15
today_temp_max = today_temp["max"]-273.15
tomorrow_temp = tomorrow_forecast["temp"]
tomorrow_temp_min = tomorrow_temp["min"]-273.15
tomorrow_temp_max = tomorrow_temp["max"]-273.15

# get precipitation/rain/snow
tomorrow_prob_prec = tomorrow_forecast["pop"]
if tomorrow_prob_prec > 0:
    vol_prec = tomorrow_forecast["rain"]
else:
    vol_prec = 0

# get UV index values
today_uv_index = today_forecast["uvi"]
tomorrow_uv_index = tomorrow_forecast["uvi"]

# print results
print( "Current temperature (C) = " + 
        str(round(current_temp, 1)))
print( "Current feels like temperature (C) = " + 
        str(round(current_feelslike, 1)))

print( "Today's UV index = " + 
        str(round(today_uv_index, 1)))
print( "Tomorrow's UV index = " + 
        str(round(tomorrow_uv_index, 1)))

# print tomorrow's precipitation values
message = (datetime.datetime.fromtimestamp(
            int(tomorrow_forecast["dt"])).strftime('%Y-%m-%d %H:%M:%S') + 
            " - Probability of precipitation = " + 
            str(round(tomorrow_prob_prec * 100)) +
            "%, Volume of precipitation  = " + 
            str(vol_prec) + "mm/h")

print (message)
