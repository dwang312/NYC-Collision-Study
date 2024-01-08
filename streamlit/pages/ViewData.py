import pandas as pd
import streamlit as st

@st.cache_data

def load_data(fp):
    #read the data
    df = pd.read_csv(fp)
    
    #convert the collumns to datetime
    df['CRASH DATE'] = pd.to_datetime(df['CRASH DATE'])
    df['CRASH TIME'] = pd.to_datetime(df['CRASH TIME'])

    return df

#fp = 'https://media.githubusercontent.com/media/dwang312/NYC-Collision-Study/main/data/NYC-CollisionZonesWeather-Jun2012-Dec2023.csv'
fp = '../data/NYC-CollisionZonesWeather-Jun2012-Dec2023.csv'
df = load_data(fp)

st.dataframe(df, width=725, height=400)