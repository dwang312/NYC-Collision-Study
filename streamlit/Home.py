import streamlit as st
import pandas as pd
import numpy as np
from st_pages import Page, show_pages, add_page_title

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

#https://discuss.streamlit.io/t/new-package-st-pages-change-page-names-and-icons-in-sidebar-without-changing-filenames/33969
show_pages(
    [
        Page("Home.py", "Home", ":house:"),
        Page("pages/About.py" , "About", ":wave:"),
        Page("pages/ViewData.py", "View Data", ":eyes:"),
        Page("pages/CollisionVisualization.py", "Collision Visualization", ":bar_chart:"),
        Page("pages/MapVisualization.py", "Map Visualization", ":world_map:"),
    ]
)

# Create a page header
st.header(" 👋")
st.markdown('<a href="/About">About</a>', unsafe_allow_html=True)