import pickle
import train1 as t1

with open(t1.model_pkl_file, "rb") as file:
    model = pickle.load(file)


sample_data = [[30.7, 19.2, 39.2, 1.4, 5.7, 18.0, 22.4, 3.8]]
predicted_aqi = model.predict(sample_data)

print(f"Predicted AQI for the given input: {predicted_aqi[0]*0.18}")