import folium
import pandas as pd
import geopandas as gpd
import streamlit as st

from streamlit_folium import st_folium
#https://folium.streamlit.app/

@st.cache_data
def load_data(zone,zip,collision):
    #read the data
    df = pd.read_csv(collision)
    zoneData = gpd.read_file(zone)
    zipData = gpd.read_file(zip)

    return zoneData, zipData, df

zoningRaw = 'https://raw.githubusercontent.com/dwang312/NYC-Collision-Study/main/data/NYC-ZoningDistrict-Geodata.json'
zipcodeRaw = 'https://raw.githubusercontent.com/dwang312/NYC-Collision-Study/main/data/NYC-ZipCode-Geodata.geojson'
fp = 'https://media.githubusercontent.com/media/dwang312/NYC-Collision-Study/main/data/NYC-CollisionZonesWeather-Jun2012-Dec2023.csv'

mapInteractive = folium.Map(location=[40.71, -74.00], 
                      zoom_start=11, 
                      tiles = 'OpenStreetMap')

zone, zipcodes, df = load_data(zoningRaw,zipcodeRaw,fp)

st_data = st_folium(mapInteractive, width=725)