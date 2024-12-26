import requests

# Function to display weather details
def display_weather(climate:str, temp: float, pressure: float, humidity:float):
    print("Todays-Weather-Report")
    print(f"Climate:{climate}\nTemperature:{temp}\nPressure:{pressure}\nHumidity:{humidity}")

# Function to fetch weather details
def fetch_weather(url:str):
    try: 
        response = requests.get(url)
        data = response.json()
        # Extracting data from json
        weather_description = data['weather'][0]['main']
        temperature = data['main']['temp']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        display_weather(
            weather_description,
            temperature,
            pressure,
            humidity
            )
    except Exception as e:
       print(f"Error:\n{e}")

def weather_detail():
    API_KEY = "075505366a631c4a757d57b90cdab792"
    City = "Guwahati"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={City}&appid={API_KEY}&units=metric" 
    fetch_weather(url)

