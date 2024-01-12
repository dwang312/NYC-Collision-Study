import pandas as pd
import streamlit as st
from pathlib import Path

st.set_page_config(layout="wide")

@st.cache_data

def load_data(fp):
    #read the data
    df = pd.read_csv(fp, low_memory=False)
    
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


def select_year(df,year):
    df = df[df['Collision Datetime'].dt.year == year]

    #Removes an entry that has a zipcode entry with decimal
    df.loc[:,'ZIP CODE'] = df['ZIP CODE'].astype(str).str.split('.').str[0] 
    return df

#Dropdown menu to select year
year = st.selectbox('Select a year', 
                    options = [2012,2013,2014,2015,
                            2016,2017,2018,2019,
                            2020,2021,2022,2023],
                    )

selected_df = select_year(df,year)
startDate = selected_df['Collision Datetime'].min().strftime('%B %d, %Y at %H:%M EST')
endDate = selected_df['Collision Datetime'].max().strftime('%B %d, %Y at %H:%M EST')

col1, col2 = st.columns([1,3])
with col1:
    numOfRows = st.radio("Select how many collisions you want to see ",(10,50,100,500,1000,'All'))
    #Formating for thousands separator: https://stackoverflow.com/questions/1823058/how-to-print-a-number-using-commas-as-thousands-separators
    st.write(f'From the NYPD NYC OpenData Motor Vehicle Collision Dataset, in {year}, the first collision report was made on {startDate} and the last reported made in {year} was on {endDate}')
    st.write(f'In {year}, New York City had {selected_df.shape[0]:,} collisions reported.')
with col2:
    st.dataframe(selected_df if numOfRows == 'All' else selected_df.iloc[:numOfRows], width=1400)
