import streamlit as st
import pandas as pd

from joblib import dump, load

def get_prediction_data(time,borough,reason)->list:
    afternoon = evening = morning = night = 0
    bronx = brooklyn = manhattan = queens = staten_island = 0
    dui = driver_negligence = oversized_vehicle = pedestrian_error = 0
    unsafe_driving_conditions = unspecified = vehicle_failure = vehicle_vandalism = 0

    if time == 'Morning (05:00 - 12:00)':
        morning = 1
        afternoon = 0
        evening = 0
        night = 0
    elif time == 'Afternoon (12:00 - 17:00)':
        morning = 0
        afternoon = 1
        evening = 0
        night = 0
    elif time == 'Evening (17:00 - 21:00)':
        morning = 0
        afternoon = 0
        evening = 1
        night = 0
    elif time == 'Night (21:00 - 05:00)': 
        morning = 0
        afternoon = 0
        evening = 0
        night = 1
    elif borough == 'Bronx':
        bronx = 1
        brooklyn = 0
        manhattan = 0
        queens = 0
        staten_island = 0
    elif borough == 'Brooklyn':
        bronx = 0
        brooklyn = 1
        manhattan = 0
        queens = 0
        staten_island = 0
    elif borough == 'Manhattan':
        bronx = 0
        brooklyn = 0
        manhattan = 1
        queens = 0
        staten_island = 0
    elif borough == 'Queens':
        bronx = 0
        brooklyn = 0
        manhattan = 0
        queens = 1
        staten_island = 0
    elif borough == 'Staten Island':
        bronx = 0
        brooklyn = 0
        manhattan = 0
        queens = 0
        staten_island = 1
    elif reason == 'DUI':
        dui = 1
        driver_negligence = 0
        oversized_vehicle = 0
        pedestrian_error = 0
        unsafe_driving_conditions = 0
        unspecified = 0
        vehicle_failure = 0
        vehicle_vandalism = 0
    elif reason == 'Driver Negligence':
        dui = 0
        driver_negligence = 1
        oversized_vehicle = 0
        pedestrian_error = 0
        unsafe_driving_conditions = 0
        unspecified = 0
        vehicle_failure = 0
        vehicle_vandalism = 0
    elif reason == 'Oversized Vehicle':
        dui = 0
        driver_negligence = 0
        oversized_vehicle = 1
        pedestrian_error = 0
        unsafe_driving_conditions = 0
        unspecified = 0
        vehicle_failure = 0
        vehicle_vandalism = 0
    elif reason == 'Pedestrian Error':
        dui = 0
        driver_negligence = 0
        oversized_vehicle = 0
        pedestrian_error = 1
        unsafe_driving_conditions = 0
        unspecified = 0
        vehicle_failure = 0
        vehicle_vandalism = 0
    elif reason == 'Unsafe Driving Condtions':
        dui = 0
        driver_negligence = 0
        oversized_vehicle = 0
        pedestrian_error = 0
        unsafe_driving_conditions = 1
        unspecified = 0
        vehicle_failure = 0
        vehicle_vandalism = 0
    elif reason == 'Unspecified':
        dui = 0
        driver_negligence = 0
        oversized_vehicle = 0
        pedestrian_error = 0
        unsafe_driving_conditions = 0
        unspecified = 1
        vehicle_failure = 0
        vehicle_vandalism = 0
    elif reason == 'Vehicle Failure':
        dui = 0
        driver_negligence = 0
        oversized_vehicle = 0
        pedestrian_error = 0
        unsafe_driving_conditions = 0
        unspecified = 0
        vehicle_failure = 1
        vehicle_vandalism = 0
    elif reason == 'Vehicle Vandalism':
        dui = 0
        driver_negligence = 0
        oversized_vehicle = 0
        pedestrian_error = 0
        unsafe_driving_conditions = 0
        unspecified = 0
        vehicle_failure = 0
        vehicle_vandalism = 1
    
    return [afternoon, evening, morning, night, 
            bronx, brooklyn, manhattan, queens, staten_island, 
            dui, driver_negligence, oversized_vehicle, pedestrian_error, 
            unsafe_driving_conditions, 
            unspecified, vehicle_failure, vehicle_vandalism]

#load the model
model = load('../model/randomUnderSamplerModel.joblib')

#user input to make a prediction
time = st.radio('Pick part of day', ['Morning (05:00 - 12:00)', 'Afternoon (12:00 - 17:00)', 
                                     'Evening (17:00 - 21:00)', 'Night (21:00 - 05:00)'])
borough = st.radio('Select the borough where the collision happened', 
                   ['Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island'])

reason = st.radio('Select the reason for the collision',['DUI', 'Driver Negligence', 'Oversized Vehicle',
       'Pedestrian Error', 'Unsafe Driving Condtions', 'Unspecified',
       'Vehicle Failure', 'Vehicle Vandalism'])

#makes prediction based on the input
make_prediction = st.button('Submit and make prediction')

if make_prediction:
    to_predict = get_prediction_data(time,borough,reason)

    #makes prediction
    prediction = model.predict([to_predict])

    #get the predicted probability
    prediction_proba = model.predict_proba([to_predict])

    #debugging help
    print(prediction_proba)

    value = prediction [0]