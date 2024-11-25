


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler



data = pd.read_csv('powerconsumption.csv')

# Check for missing values
print(data.isnull().sum())

# Fill missing values (if any)
data.fillna(method='ffill', inplace=True)

# Normalize continuous features
scaler = StandardScaler()
data[['Temperature', 'Humidity']]=scaler.fit_transform(data[['Temperature', 'Humidity']])

# Visualize data
sns.pairplot(data, diag_kind='kde')
plt.show()

"""2. Build a Machine Learning Model
● Split the dataset into training and testing sets.
● Use a regression algorithm (e.g., Ridge Regression) to predict energy consumption.
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

# Split data
X = data[['Temperature', 'Humidity']]
y = data['PowerConsumption_Zone1']
X_train, X_test, y_train, y_test = train_test_split(X, y,
test_size=0.2, random_state=42)

# Train model
model = Ridge()
model.fit(X_train, y_train)

# Test model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

print(f'Mean Squared Error: {mse}')

"""3. Build a Streamlit App
● Create an interactive app for users to input features and get predictions.
"""

# Install streamlit if not already installed


# Import necessary libraries
import streamlit as st
import numpy as np

# Streamlit app
st.title("Power Consumption Prediction")

# Input fields
temperature = st.number_input("Temperature (°C)")
humidity = st.number_input("Humidity (%)")

# Prediction button
if st.button("Predict"):
    # Make prediction
    input_features = np.array([[temperature, humidity, occupancy]]) # Indented this line to be inside the if block
    prediction = model.predict(input_features)[0]
    st.write(f"Predicted Energy Consumption: {prediction:.2f} kWh")



"""4. Deployment
Save the model as a pickle file:
"""

import joblib
joblib.dump(model, 'ridge_model.pkl')
