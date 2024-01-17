import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title = "About",
    page_icon = "👋",
)

st.write("# A NYC Motor Vehicle Collision Study")

important_links = '''
[Github Repository](https://github.com/dwang312/NYC-Collision-Study)

[Linkedin](https://www.linkedin.com/in/david-wang-nyc/)
'''

st.markdown(important_links)

st.markdown(
    '''
# Data Information

The [NYC Open Data - Motor Vehicile Collisions  (Crashes) Dataset](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95) contains information on collisions reported by the NYPD that involves where someone is injured or killed, or where there is at least $1000 worth of damage.

- The dataset contains 29 columns and about 2 million rows and counting.  It contains records from July 1st, 2012 to present.

[NYC Open Data - Motor Vehicle Collisions (Vehicles)](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Vehicles/bm4k-52h4)

[NYC Open Data - Motor Vehicle Collisions (Person)](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Person/f55k-p6yu)


The [NYC GIS Zoning Data](https://www.nyc.gov/site/planning/data-maps/open-data/dwn-gis-zoning.page#metadata) 
was developed by the NYC Planning department and provides information on zoning districts in NYC. We will be using data for map visualizatins and to analyze our Motor Vehicile Collisions  (Crashes) Dataset.
'''
)
