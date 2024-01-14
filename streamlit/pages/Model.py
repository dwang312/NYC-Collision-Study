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
    elif time == 'Afternoon (12:00 - 17:00)':
        afternoon = 1
    elif time == 'Evening (17:00 - 21:00)':
        evening = 1
    elif time == 'Night (21:00 - 05:00)':
        night = 1
    elif borough == 'Bronx':
        bronx = 1
    elif borough == 'Brooklyn':
        brooklyn = 1
    elif borough == 'Manhattan':
        manhattan = 1
    elif borough == 'Queens':
        queens = 1
    elif borough == 'Staten Island':
        staten_island = 1
    elif reason == 'DUI':
        dui = 1
    elif reason == 'Driver Negligence':
        driver_negligence = 1
    elif reason == 'Oversized Vehicle':
        oversized_vehicle = 1
    elif reason == 'Pedestrian Error':
        pedestrian_error = 1
    elif reason == 'Unsafe Driving Conditions':
        unsafe_driving_conditions = 1
    elif reason == 'Unspecified':
        unspecified = 1
    elif reason == 'Vehicle Failure':
        vehicle_failure = 1
    elif reason == 'Vehicle Vandalism':
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
    print(prediction_proba) #[0,1]
    value = prediction[0]
    print(prediction)
    
    noInjury = prediction_proba[0][0]
    injury = prediction_proba[0][1]
    if value:
        st.write('There is a **{}%** chance that this collision will result in an injury'.format(round(injury*100,2)))
    else:
        st.write('There is a **{}%** chance that this collision will not result in an injury'.format(round(noInjury*100,2)))
