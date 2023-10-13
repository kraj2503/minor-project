from flask import Flask, render_template, request
import try1

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = []
    if request.method == 'POST':
        city = request.form['city']
        days = int(request.form['days'])

        # Fetch the data for the given city and days
        api_response = try1.get_api_response(city, days)
        
        # Process and predict AQI for current data
        try:
            current_data = try1.extract_data(api_response['current'])
            current_aqi = try1.predict_aqi(current_data)
            output.append(f"Current AQI: {current_aqi:.2f}")  # AQI up to 2 decimal places
        except KeyError:
            pass

        # Extract data for forecast days (excluding the first forecast)
        for forecast_day in api_response['forecast']['forecastday'][1:]:
            try:
                forecast_data = try1.extract_data(forecast_day)
                forecast_aqi = try1.predict_aqi(forecast_data)
                output.append(f"AQI for {forecast_day['date']}: {forecast_aqi:.2f}")  # AQI up to 2 decimal places
            except KeyError:
                pass

    return render_template('index.html', output=output)

if __name__ == "__main__":
    app.run(debug=True)
