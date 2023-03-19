import requests

API_KEY = "20f3041b6708329273061e8786e9ece9"

base_url = "https://api.openweathermap.org/data/2.5/weather?"

city = input("Enter the name of your city: ")

concatenated_url = base_url + "q="+ city + "&appid="+API_KEY 

response = requests.get(concatenated_url)

a = response.json()

if a["cod"]==200:

    # Weather
    weatherDescription = a["weather"][0]["description"]

    # Temp
    b = a['main']
    current_temperature = b["temp"]
    TempMin = b["temp_min"]
    TempMax = b["temp_max"]
    current_pressure = b["pressure"]
    current_humidity = b["humidity"]

    # wind
    c = a["wind"]
    current_wind_speed = c["speed"]

    # Printing out data
    print(f"Atmosphere/Weather Description : {weatherDescription}\n")
    print(f"Temperature : {current_temperature}\n")
    print(f"Today's Maximum temperature : {TempMax}\n")
    print(f"Today's Minimum temperature : {TempMin}\n")
    print(f"Pressure : {current_pressure}\n")
    print(f"Humidity : {current_humidity}\n")
    print(f"Wind Speed : {current_wind_speed}\n")

else:
    print("Seems like you have entered a wrong city!\n TRY AGAIN")