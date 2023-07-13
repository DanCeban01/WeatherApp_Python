import requests
from datetime import datetime

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"  # You can change the units to imperial if you prefer Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return None

def main():
    api_key = "4cac3f7ef1fcf872d853dba3ddec59ce"  # Replace with your actual API key
    location = input("Enter a location: ")
    weather_data = get_weather(api_key, location)

    if weather_data:
        main_weather = weather_data["weather"][0]["main"]
        description = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("Weather in", location)
        print("Time:", current_time)
        print("Main weather:", main_weather)
        print("Description:", description)
        print("Temperature:", temperature, "°C")
        print("Humidity:", humidity, "%")
    else:
        print("Failed to retrieve weather data.")

if __name__ == "__main__":
    main()
