import requests
def weather_details(city,api_key):
    url = "https://api.openweathermap.org/data/2.5/weather?"
    final_url = f"{url}q={city}&appid={api_key}"
    try:
        response = requests.get(final_url)
        response.raise_for_status()
        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        feel_like = data["main"]["feels_like"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}")
        print(f"Humidity:{humidity}%")
        print(f"Desciption: {data['weather'][0]['description'].capitalize()}")
#
#
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

weather_details("jaipur","d8f2081ab27a8b0320c06b1f5a0907f3")