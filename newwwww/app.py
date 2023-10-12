from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Load trained model from the pickle file
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    sample = [[data['co'], data['no2'], data['o3'], data['so2'], data['pm2_5'], data['pm10'], data['temp'], data['humidity']]]
    prediction = model.predict(sample)
    return jsonify({'AQI': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
