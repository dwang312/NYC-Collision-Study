import pandas as pd
import streamlit as st

@st.cache_data

def load_data(fp):
    #read the data
    df = pd.read_csv(fp)
    
    #convert the collumns to datetime
    df['CRASH DATE'] = pd.to_datetime(df['CRASH DATE'] + ' ' + df['CRASH TIME'])
    df.drop('CRASH TIME',axis= 1, inplace=True)
    df.rename(columns={"CRASH DATE": "Collision Datetime"}, inplace=True)

    useful_cols=['Collision Datetime', 'BOROUGH', 'ZIP CODE', 'LATITUDE',
       'LONGITUDE', 'LOCATION','ON STREET NAME','CROSS STREET NAME', 'NUMBER OF PERSONS INJURED',
       'NUMBER OF PERSONS KILLED', 'NUMBER OF PEDESTRIANS INJURED',
       'NUMBER OF PEDESTRIANS KILLED', 'NUMBER OF CYCLIST INJURED',
       'NUMBER OF CYCLIST KILLED', 'NUMBER OF MOTORIST INJURED',
       'NUMBER OF MOTORIST KILLED', 'CONTRIBUTING FACTOR VEHICLE 1',
       'CONTRIBUTING FACTOR VEHICLE 2','COLLISION_ID', 'VEHICLE TYPE CODE 1', 'VEHICLE TYPE CODE 2']
    df=df[useful_cols]

    drop_null_cols=['Collision Datetime', 'BOROUGH', 'ZIP CODE', 'LATITUDE',
       'LONGITUDE','CONTRIBUTING FACTOR VEHICLE 1','NUMBER OF PERSONS INJURED',
       'NUMBER OF PERSONS KILLED','VEHICLE TYPE CODE 1']
    df = df.dropna(subset=drop_null_cols).reset_index(drop=True)

    return df

#fp = 'https://media.githubusercontent.com/media/dwang312/NYC-Collision-Study/main/data/NYC-CollisionZonesWeather-Jun2012-Dec2023.csv'
#fp = '../data/NYC-CollisionZonesWeather-Jun2012-Dec2023.csv'

fp = '../data/Motor_Vehicle_Collisions_-_Crashes_20231202.csv'

df = load_data(fp)

year = st.selectbox('Select a year', 
                    options = [2012,2013,2014,2015,
                            2016,2017,2018,2019,
                            2020,2021,2022,2023],
                    )

def select_year(df,year):
    df = df[df['Collision Datetime'].dt.year == year]
    return df

selected_df = select_year(df,year)

st.dataframe(selected_df,width = 1400)