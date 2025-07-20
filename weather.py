import requests
API_KEY = '323faca00de64b0c8df163721240210' 
BASE_URL = "http://api.weatherapi.com/v1/current.json"

def get_weather(city_name):
    # Building the request URL
    complete_url = f"{BASE_URL}?key={API_KEY}&q={city_name}&aqi=no"

    # Sending the HTTP request
    response = requests.get(complete_url)

    # Extracting data in JSON format
    data = response.json()

    # Print the entire response for debugging
    print("Response from API:", data)

    # Checking if the city was found
    if 'error' not in data:
        # Extracting the necessary data
        current = data["current"]
        temperature = current["temp_c"]
        humidity = current["humidity"]
        condition = current["condition"]["text"]
        wind_speed = current["wind_kph"]

        # Displaying the results
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition}")
        print(f"Wind Speed: {wind_speed} kph")
    else:
        # Print full error message if city is not found or other errors occur
        print(f"Error: {data['error']['message']}. City not found.")

# Main function
def main():
    print("Weather Forecast Application")
    city_name = input("Enter city name: ")
    get_weather(city_name)

if __name__ == "__main__":
    main()
