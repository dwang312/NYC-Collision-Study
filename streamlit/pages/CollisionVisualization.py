import streamlit as st

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

import json
import datetime
import calendar

st.set_page_config(layout="wide")

@st.cache_data

def load_colision_data(fp):
    #read in the csv via the link
    df = pd.read_csv(fp)

    #convert the collumns to datetime
    df['CRASH DATE'] = pd.to_datetime(df['CRASH DATE'])
    df['CRASH TIME'] = pd.to_datetime(df['CRASH TIME'])

    return(df)

#loading the data
#fp = 'https://media.githubusercontent.com/media/dwang312/NYC-Collision-Study/main/data/NYC-CollisionZonesWeather-Jun2012-Dec2023.csv'
df = load_colision_data(fp)




c2018 = df['CRASH DATE'].dt.year == 2018
c2019 = df['CRASH DATE'].dt.year == 2019
c2020 = df['CRASH DATE'].dt.year == 2020
c2021 = df['CRASH DATE'].dt.year == 2021
c2022 = df['CRASH DATE'].dt.year == 2022
df2018to2021 = df[c2018 | c2019 | c2020 | c2021 ]

# Group by both year and month, then count occurrences
value_counts = df2018to2021.groupby([df2018to2021['CRASH DATE'].dt.year.rename('Year'), df2018to2021['CRASH DATE'].dt.month.rename('Month')]).size().reset_index(name='Counts')
value_counts['Month'] = value_counts['Month'].apply(lambda x: calendar.month_abbr[x])
value_counts['Month and Year'] = value_counts['Month'] + ' ' + value_counts['Year'].astype(str)
value_counts.drop(['Year', 'Month'], axis=1, inplace=True)
value_counts = value_counts[['Month and Year', 'Counts']]


# Assuming 'Month and Year' is a column in your DataFrame 'value_counts'
value_counts['Month and Year'] = pd.to_datetime(value_counts['Month and Year'], format='%b %Y')


fig = px.line(value_counts, x='Month and Year', y='Counts',
              hover_data={"Month and Year": True},
              markers=True,
              color_discrete_sequence=px.colors.sequential.Viridis,
              template="plotly_white").update_layout(
                  title={
                      'text': 'Crashes by Month (Jan 2018 - Dec 2021)',
                      'x': 0.5,  # Set x to 0.5 for center alignment
                      'xanchor': 'center',  # Set xanchor to center
                  },
                  width=900,
                  height=600
              ).update_xaxes(
                            tickvals=value_counts['Month and Year'][::3],  # Set ticks to every 3rd month
                            tickformat="%b %Y",  # Format ticks as month abbreviation and year
                            tickangle=45,  # Rotate tick labels for better readability (if needed)
                            tickmode='array',  # Set the mode to display specified tickvals
              )

# Highlighting the specific date (March 19th, 2020)
critical_date = '2020-03-01'
critical_count = value_counts[value_counts['Month and Year'] == critical_date]['Counts'].values[0]

# Choosing a color from Viridis color scale
highlight_color = px.colors.sequential.Viridis[4]  # Change the index as needed

fig.add_scatter(x=[critical_date],
                y=[value_counts[value_counts['Month and Year'] == critical_date]['Counts'].values[0]],
                mode='markers',
                marker=dict(color="red", size=10),
                name='NYC - COVID')

# Get the maximum count for setting y1 in add_shape
max_count = value_counts['Counts'].max()

fig.add_shape(
    type="line",
    x0=critical_date, y0=0,
    x1=critical_date, y1=max_count,
    line=dict(color="grey", width=1, dash="dash"),
)

fig.update_yaxes(title_text="Number of Crashes")

st.plotly_chart(fig, use_container_width=True)