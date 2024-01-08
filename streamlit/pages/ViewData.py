import pandas as pd
import streamlit as st

@st.cache_data

def load_data(fp):
    #read the data
    df = pd.read_csv(fp)

    return df

fp = 'https://media.githubusercontent.com/media/dwang312/NYC-Collision-Study/main/data/NYC-CollisionZonesWeather-Jun2012-Dec2023.csv'
df = load_data(fp)

st.DataFrame(df, width=725, height=400)