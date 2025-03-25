import requests

def get_weather_data(lat, lon, api_key):
    """Fetch weather data from OpenWeatherMap API."""
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def main():
    """Main function to get user input and fetch weather data."""
    api_key = "c5d2ac0f1b978e9f90b03cc188d90142"
    try:
        lat = float(input("Enter latitude: "))
        lon = float(input("Enter longitude: "))
    except ValueError:
        print("Error: Please enter valid numeric values for latitude and longitude.")
        return

    weather_data = get_weather_data(lat, lon, api_key)
    if weather_data:
        print("Weather Data:")
        print(weather_data)

if __name__ == "__main__":
    main()

