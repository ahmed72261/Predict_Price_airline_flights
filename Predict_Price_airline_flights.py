# Import necessary libraries
import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the trained XGBoost model
model = joblib.load('XGBoost_best_model.joblib')

# Mapping for Airline and Destination
airline_mapping = {0: 'Trujet', 1: 'SpiceJet', 2: 'Air Asia', 3: 'IndiGo', 4: 'GoAir', 5: 'Vistara',
                    6: 'Vistara Premium economy', 7: 'Air India', 8: 'Multiple carriers',
                    9: 'Multiple carriers Premium economy', 10: 'Jet Airways', 11: 'Jet Airways Business'}

destination_mapping = {0: 'Kolkata', 1: 'Hyderabad', 2: 'Delhi', 3: 'Banglore', 4: 'Cochin'}

# Function to make predictions
def predict_price(airline, destination, total_stops, journey_day,journey_month,dep_time_hour,dep_time_minute,
                arrival_time_hour, arrival_time_minute, duration_hours,duration_mins,
                source_banglore, source_kolkata,source_delhi, source_chennai, source_mumbai):
    input_data = {
        'Airline': airline_mapping.get(airline),
        'Destination': destination_mapping.get(destination),
        'Total_Stops': total_stops,
        'journey_day': journey_day,
        'journey_month': journey_month,
        'Dep_Time_hour': dep_time_hour,
        'Dep_Time_minute': dep_time_minute,
        'Arrival_Time_hour': arrival_time_hour,
        'Arrival_Time_minute': arrival_time_minute,
        'Duration_hours': duration_hours,
        'Duration_mins': duration_mins,
        'Source_Banglore': source_banglore,
        'Source_Kolkata': source_kolkata,
        'Source_Delhi': source_delhi,
        'Source_Chennai': source_chennai,
        'Source_Mumbai': source_mumbai,
    }
    features = pd.DataFrame([input_data])
    prediction = model.predict(features)[0]
    return prediction

# Streamlit app
st.title("Flight Price Prediction App")

# Input features from the user
airline = st.selectbox("Select Airline", list(airline_mapping.values()))
destination = st.selectbox("Select Destination", list(destination_mapping.values()))
total_stops = st.number_input("Enter Total Stops", min_value=0, max_value=4, value=0)
journey_month = st.number_input("Enter Journey Month", min_value=1, max_value=12, value=1)
journey_day = st.number_input("Enter Journey Day", min_value=1, max_value=31, value=1)
source_delhi = st.number_input("Enter Source Delhi (1 for Yes, 0 for No)", min_value=0, max_value=1, value=0)
source_banglore = st.number_input("Enter Source Banglore (1 for Yes, 0 for No)", min_value=0, max_value=1, value=0)
source_kolkata = st.number_input("Enter Source Kolkata (1 for Yes, 0 for No)", min_value=0, max_value=1, value=0)
source_chennai = st.number_input("Enter Source Chennai (1 for Yes, 0 for No)", min_value=0, max_value=1, value=0)
source_mumbai = st.number_input("Enter Source Mumbai (1 for Yes, 0 for No)", min_value=0, max_value=1, value=0)
arrival_time_hour = st.number_input("Enter Arrival Time Hour", min_value=0, max_value=23, value=0)
arrival_time_minute = st.number_input("Enter Arrival Time Minute", min_value=0, max_value=59, value=0)
dep_time_hour = st.number_input("Enter Departure Time Hour", min_value=0, max_value=23, value=0)
dep_time_minute = st.number_input("Enter Departure Time Minute", min_value=0, max_value=59, value=0)
duration_hours = st.number_input("Enter Duration Hours", min_value=0, max_value=23, value=1)
duration_mins = st.number_input("Enter Duration Minutes", min_value=0, max_value=59, value=0)

# Make a prediction and display the result
if st.button("Predict Price"):
    result = predict_price(airline, destination, total_stops, journey_day,journey_month,dep_time_hour,dep_time_minute,
                            arrival_time_hour, arrival_time_minute, duration_hours,duration_mins,
                            source_banglore, source_kolkata,source_delhi, source_chennai, source_mumbai)
    st.success(f"The predicted price is: {result:.2f} INR")

