import folium
import pandas as pd
import geopandas as gpd
import streamlit as st

from streamlit_folium import st_folium
#https://folium.streamlit.app/

from Home import load_config

st.set_page_config(layout="wide")

config = load_config()


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

    # zip_gb = folium.features.GeoJson(
    #     geo_zipdf,
    #     style_function=style_function, 
    #     control=False,
    #     highlight_function=highlight_function, 
    #     tooltip=folium.features.GeoJsonTooltip(
    #         fields=['ZIP CODE', 'Percentage Per Borough'],
    #         aliases=['Zip Code', 'Percentage Per Borough '],
    #         style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;"),
    #     )
    # )
    
    zip_gb = folium.features.GeoJson(
        zipcodes,
        style_function=style_function, 
        control=False,
        highlight_function=highlight_function, 
    )

    mapInteractive.add_child(zip_gb)

def load_zoning(mapInteractive,zone,zoningID):
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

def load_trucking(mapInteractive, truck_routes):
    truck_routes = gpd.read_file(truck_routes)
    print("Accessing Truck Routes")
    truck_routes_shape = folium.features.GeoJson(
        truck_routes,
    )
    mapInteractive.add_child(truck_routes_shape)




#Load Data
zoningRaw = config['paths']['zoning_raw']
zoningIDRaw = config['paths']['zoning_id_raw']
zipcodeRaw = config['paths']['zipcode_raw']
fp = config['paths']['collision_zones_weather']
truck_routes = config['paths']['truck_routes']

base = st.selectbox('Select a base map provider',["OpenStreetMap", "CartoDB Positron", "CartoBD Voyager"])

mapInteractive = folium.Map(location=[40.71, -74.00], 
                      zoom_start=11, 
                      tiles = base)

zone, zoningID, zipcodes, df = load_data(zoningRaw,zoningIDRaw,zipcodeRaw,fp)
option = st.radio('Select a layer to display',["None","Zoning", "Zipcode","Truck Routes"])

if option == "None":
    pass
elif option == "Zoning":
    load_zoning(mapInteractive,zone,zoningID)
elif option == "Zipcode":
    load_ziplayer(mapInteractive,df,zipcodes)
elif option == "Truck Routes":
    load_trucking(mapInteractive,truck_routes)

folium.LayerControl().add_to(mapInteractive) 

st_data = st_folium(mapInteractive,  width=1500, height=800)