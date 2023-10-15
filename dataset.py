import pandas as pd
import numpy as np

# Set a seed for reproducibility
np.random.seed(42)

# Number of records
n_records = 10000

# Generate data based on the defined range and statistical properties
data = {
    "co": np.random.uniform(0, 10, n_records),
    "no2": np.random.uniform(0, 50, n_records),
    "o3": np.random.uniform(0, 150, n_records),
    "so2": np.random.uniform(0, 20, n_records),
    "pm2_5": np.random.uniform(0, 150, n_records),
    "pm10": np.random.uniform(0, 300, n_records),
    "temp": np.random.uniform(-10, 40, n_records),
    "humidity": np.random.uniform(0, 100, n_records)
}

# Create a DataFrame
df_air_quality = pd.DataFrame(data)

# Save the DataFrame to CSV format
df_air_quality.to_csv("air_quality_data.csv", index=False)
