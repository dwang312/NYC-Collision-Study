import streamlit as st
import pandas as pd
import numpy as np
from st_pages import Page, Section, show_pages, add_page_title

#Can be standarize
#https://medium.com/analytics-vidhya/how-to-write-configuration-files-in-your-machine-learning-project-47bc840acc19

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

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
    ]
)

st.markdown('<a href="/About">About</a>', unsafe_allow_html=True)