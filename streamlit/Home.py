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
    print("Full path to config.yaml:", config_file_path)

    # Load configuration from file
    with open(config_file_path, 'r') as config_file:
        config = yaml.safe_load(config_file)
    
    return config


#Can be standarize
#https://medium.com/analytics-vidhya/how-to-write-configuration-files-in-your-machine-learning-project-47bc840acc19

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

load_config()

# Create a page header
add_page_title()

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

st.markdown('<a href="/About">About</a>', unsafe_allow_html=True)