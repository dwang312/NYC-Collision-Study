import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title = "(TEMP)",
    page_icon = "👋",
)

st.write("# Welcome to (PROJECT NAME)")

important_links = '''
[Github Repository]()

[Linkedin](https://www.linkedin.com/in/david-wang-nyc/)
'''

st.markdown(important_links)