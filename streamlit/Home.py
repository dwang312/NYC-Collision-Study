import streamlit as st
import pandas as pd
import numpy as np
from st_pages import Page, Section, show_pages, add_page_title

import yaml
import os

def load_config():
    # Get the path to the YAML file (located in the root directory)
    config_file_path = os.path.join(os.path.dirname((os.path.dirname(os.path.abspath(__file__)))),'config.yaml')

    # Print the full path for debugging
    #print("Full path to config.yaml:", config_file_path)

    # Load configuration from file
    with open(config_file_path, 'r') as config_file:
        config = yaml.safe_load(config_file)
    
    return config

st.set_page_config(
    layout="wide",
    page_title="NYC MV Collision Study",
    page_icon="🚗",
)

load_config()

#https://discuss.streamlit.io/t/new-package-st-pages-change-page-names-and-icons-in-sidebar-without-changing-filenames/33969
show_pages(
    [
        Page("Home.py", "Home", ":house:", in_section=False),
        Page("pages/About.py" , "About", ":wave:", in_section=False), 
        Section("Data Exploration", ":bar_chart:"),
        Page("pages/Exploratory.py", "Exploratory Questions", ":bar_chart:"),
        Page("pages/ViewData.py", "View Data", ":eyes:"),
        Page("pages/CollisionVisualization.py", "Collision Visualization", ":bar_chart:"),
        Page("pages/MapVisualization.py", "Map Visualization", ":world_map:"),
        Page("pages/Model.py", "Model", ":bar_chart:"),
    ]
)

st.markdown('''
            <div align ="center">
                <h1>NYC Motor Vehicle Collision Study</h1>
            </div>
            ''', unsafe_allow_html=True)
col1,col2,col3 = st.columns([1,5,1])
with col2:
    st.image('images/bk_collision.png')
    st.markdown('''<div align ="center">
                    <a href="/About">Click to Learn More</a>
                </div>
            ''', unsafe_allow_html=True)
