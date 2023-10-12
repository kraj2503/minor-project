import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load the dataset from CSV
df_air_quality = pd.read_csv("air_quality_data.csv")

# Compute pseudo-AQI
weights = {
    "co": 0.4,
    "no2": 0.5,
    "o3": 1.1,
    "so2": 1.3,
    "pm2_5": 5.5,
    "pm10": 4.4
}
df_air_quality["pseudo_AQI"] = sum(df_air_quality[pollutant] * weight for pollutant, weight in weights.items())

# Splitting the data into training and test sets (80% train, 20% test)
X = df_air_quality[["co", "no2", "o3", "so2", "pm2_5", "pm10", "temp", "humidity"]]
y = df_air_quality["pseudo_AQI"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the Random Forest regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Sample data for prediction (replace with your values)
# sample_data = [[30.7, 19.2, 39.2, 1.4, 5.7, 18.0, 22.4, 3.8]]
# predicted_aqi = model.predict(sample_data)

# # print(f"Predicted AQI for the given input: {predicted_aqi[0]*0.5}")

import pickle

# save the iris classification model as a pickle file
model_pkl_file = "AQI.pkl"

with open(model_pkl_file, "wb") as file:
    pickle.dump(model, file)
