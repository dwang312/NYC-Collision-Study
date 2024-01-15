import folium
import pandas as pd
import geopandas as gpd
import streamlit as st

from streamlit_folium import st_folium
#https://folium.streamlit.app/

from Home import load_config

config = load_config()

st.set_page_config(layout="wide")

@st.cache_data
def load_data(zone,zoneID,zip,collision):
    #read the data
    df = pd.read_csv(collision, low_memory=False)
    zoneData = gpd.read_file(zone)
    zoneID = pd.read_csv(zoneID, low_memory=False)
    zipData = gpd.read_file(zip)

    return zoneData, zoneID, zipData, df

def load_ziplayer(mapInteractive,df,zipcodes):
    gb = df.groupby(['BOROUGH','ZIP CODE']).size().reset_index(name='Count')

    # Get the total count for each borough
    borough_total = gb.groupby('BOROUGH')['Count'].sum().reset_index(name='BoroughTotal')

    # Merge the total count back to the grouped data
    gb = pd.merge(gb, borough_total, on='BOROUGH')

    # Calculate the percentage within each borough
    gb['Percentage Per Borough'] = (gb['Count'] / gb['BoroughTotal']) * 100
    gb['Percentage Per Borough'] = gb['Percentage Per Borough'].round(2)

    # Removing decimal and anything after
    gb['ZIP CODE'] = gb['ZIP CODE'].astype(str).str.split('.').str[0]

    zip_gbd = gb.merge(zipcodes, left_on='ZIP CODE', right_on='ZIPCODE', how='left')

    zip_gbd.dropna(inplace=True)
    geo_zipdf = gpd.GeoDataFrame(zip_gbd, geometry='geometry', crs='EPSG:4326')

    style_function = lambda x: {'fillColor': '#ffffff', 
                                'color':'#000000', 
                                'fillOpacity': 0.1, 
                                'weight': 0.1}
    highlight_function = lambda x: {'fillColor': '#000000', 
                                    'color':'#000000', 
                                    'fillOpacity': 0.50, 
                                    'weight': 0.1}

    zip_gb = folium.features.GeoJson(
        geo_zipdf,
        style_function=style_function, 
        control=False,
        highlight_function=highlight_function, 
        tooltip=folium.features.GeoJsonTooltip(
            fields=['ZIP CODE', 'Percentage Per Borough'],
            aliases=['Zip Code', 'Percentage Per Borough '],
            style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;"),
        )
    )
    
    # zip_gb = folium.features.GeoJson(
    #     zipcodes,
    #     style_function=style_function, 
    #     control=False,
    #     highlight_function=highlight_function, 
    # )

    mapInteractive.add_child(zip_gb)

def load_zoning(mapInteractive,zone,zoningID):

    def filterDist(dist):
        #If has a residential designation:
        if "R" in dist:
            return 0
        #If it's not residential but has a commercial designation:
        elif "C" in dist:
            return 10
        else:  #everything else, most likely manufacturing
            return 20
        
    #Apply the filter to our dataframe to create a new column:
    zoningID['District Type'] = zoningID['Zoning District'].apply(filterDist)

    zone = folium.features.GeoJson(
        zone,
        style_function=lambda x: {'color':'#000000', 
                                  'fillOpacity': 0.1, 
                                  'weight': 0.1},
        control=False,
        highlight_function= lambda x: {'fillColor': '#000000', 
                                    'color':'#000000', 
                                    'fillOpacity': 0.50, 
                                    'weight': 0.1},
        tooltip=folium.features.GeoJsonTooltip(
            fields=['ZONEDIST'],
            style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;"),
            aliases=['Zoning District: ']
        )
    )
    mapInteractive.add_child(zone)


#Load Data
zoningRaw = config['paths']['zoning_raw']
zoningIDRaw = config['paths']['zoning_id_raw']
zipcodeRaw = config['paths']['zipcode_raw']
fp = config['paths']['collision_zones_weather']

base = st.selectbox('Select a base map provider',["OpenStreetMap", "CartoDB Positron", "CartoBD Voyager", "NASAGIBS Blue Marble"])

mapInteractive = folium.Map(location=[40.71, -74.00], 
                      zoom_start=11, 
                      tiles = base)

zone, zoningID, zipcodes, df = load_data(zoningRaw,zoningIDRaw,zipcodeRaw,fp)
#load_ziplayer(mapInteractive,df,zipcodes)
load_zoning(mapInteractive,zone,zoningID)

folium.LayerControl().add_to(mapInteractive) 

st_data = st_folium(mapInteractive,  width=1500, height=800)