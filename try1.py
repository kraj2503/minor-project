import requests
import json
import pickle
# import train1 as t1

def get_api_key_from_config(file_path='config.txt'):
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith('WEATHER_API_KEY'):
                return line.split('=')[1].strip()
    return None


# API_KEY = get_api_key_from_config()


def fetch_weather_aqi_data(city,days=0):
    
    API_KEY = get_api_key_from_config()
    url = f"https://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days={days}&aqi=yes&alerts=no"
    response = requests.get(url)
    data = response.json()

    # Save the response as a JSON file
    with open(f"{city}_weather_data.json", "w") as outfile:
        json.dump(data, outfile)

    return data

def get_api_response(city, days):
    return fetch_weather_aqi_data(city, days)

def extract_data(data_dict):
    """
    Extract the required data from the given dictionary.
    """
    # Determine if we're dealing with 'current' data or 'forecast' data
    if 'day' in data_dict:
        air_quality_data = data_dict['day']['air_quality']
        temp_data = data_dict['day']['avgtemp_c']
        humidity_data = data_dict['day']['avghumidity']
    else:
        air_quality_data = data_dict['air_quality']
        temp_data = data_dict.get('temp_c', None)
        humidity_data = data_dict.get('humidity', None)
    
    return {
        'co': air_quality_data['co'],
        'no2': air_quality_data['no2'],
        'o3': air_quality_data['o3'],
        "so2": air_quality_data['so2'],
        'pm2_5': air_quality_data['pm2_5'],
        'pm10': air_quality_data['pm10'],
        'temp_c': temp_data,
        'humidity': humidity_data
    }


# Load the trained model once when the script is run
with open('model.pkl', "rb") as file:
    model = pickle.load(file)

def predict_aqi(data):
    """
    Predict AQI based on the given data using the trained model.
    """
    # Convert the data dictionary to a list format that the model expects
    sample_data = [[
        data['co'], 
        data['no2'], 
        data['o3'], 
        data['so2'],
        data['pm2_5'], 
        data['pm10'], 
        data['temp_c'], 
        data['humidity']
    ]]
    predicted_aqi = model.predict(sample_data)

    # Return the predicted AQI
    return predicted_aqi[0]*.18


