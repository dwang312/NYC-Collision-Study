import streamlit as st
import pandas as pd
import plotly.express as px
import datetime as dt
import calendar

from Home import load_config

#config = load_config()

st.set_page_config(layout="wide")

@st.cache_data

def load_colision_data(fp):
    #read in the csv via the link
    df = pd.read_csv(fp,low_memory=False)

    #convert the collumns to datetime
    df['CRASH DATE'] = pd.to_datetime(df['CRASH DATE'] + ' ' + df['CRASH TIME'])
    df.drop('CRASH TIME',axis= 1, inplace=True)
    df.rename(columns={"CRASH DATE": "Collision Datetime"}, inplace=True)

    return(df)

#loading the data
#fp = '../data/NYC-CollisionZonesWeather-Jun2012-Dec2023.csv'
fp = config['paths']['collision_zones_weather']
df = load_colision_data(fp)

def graph_years(interval):
    startYear = pd.to_datetime(interval[0])
    endYear = pd.to_datetime(interval[1])
    #filtering the data
    df_filtered = df[(df['Collision Datetime'] >= startYear) & (df['Collision Datetime'] <= endYear)]

    #grouping the data
    df_grouped = df_filtered.groupby([df_filtered['Collision Datetime'].dt.year.rename('Year'), df_filtered['Collision Datetime'].dt.month.rename('Month')]).size().reset_index(name='Counts')
    df_grouped['Month'] = df_grouped['Month'].apply(lambda x: calendar.month_abbr[x])
    df_grouped['Month and Year'] = df_grouped['Month'] + ' ' + df_grouped['Year'].astype(str)
    df_grouped.drop(['Year', 'Month'], axis=1, inplace=True)
    df_grouped = df_grouped[['Month and Year', 'Counts']]

    #plotting the data
    fig = px.line(df_grouped, x='Month and Year', y='Counts',
                hover_data={"Month and Year": True},
                markers=True,
                color_discrete_sequence=px.colors.sequential.Viridis,
                template="plotly_white").update_layout(
                    title={
                        'text': 'Crashes by Month (' + startYear.strftime(' %b %Y')+ ' - ' + endYear.strftime('%b %Y') + ')',
                        'x': 0.5,  # Set x to 0.5 for center alignment
                        'xanchor': 'center',  # Set xanchor to center
                    },
                    width=900,
                    height=600
                ).update_xaxes(
                                tickvals=df_grouped['Month and Year'][::3],  # Set ticks to every 3rd month
                                tickformat="%b %Y",  # Format ticks as month abbreviation and year
                                tickangle=45,  # Rotate tick labels for better readability (if needed)
                                tickmode='array',  # Set the mode to display specified tickvals
                ).update_yaxes(
                                title_text="Number of Crashes"
                ).update_traces(
                    line_color='#636EFA',  # Set color of line
                )
    
    #Ctl + / to uncomment
    # if 2020 in interval:
    #      # Highlighting the specific date (March 19th, 2020)
    #     critical_date = '2020-03-01'
    #     critical_count = df_grouped[df_grouped['Month and Year'] == critical_date]['Counts'].values[0]
    #     fig.add_scatter(x=[critical_date],
    #                     y=[critical_count],
    #                     mode='markers',
    #                     marker=dict(color="red", size=10),
    #                     name='NYC - COVID')
    #     # Get the maximum count for setting y1 in add_shape
    #     max_count = df_grouped['Counts'].max()

    #     fig.add_shape(
    #         type="line",
    #         x0=critical_date, y0=0,
    #         x1=critical_date, y1=max_count,
    #         line=dict(color="grey", width=1, dash="dash"),
    #     )
        
    
    return fig
   
dateInterval = st.slider('TEMP TEXT',
                         min_value = dt.datetime(2012, 6, 1),
                         max_value = dt.datetime(2023,11, 1),
                         value = (dt.datetime(2012, 6, 1),dt.datetime(2023,12,1)),
                            format = 'MMM YYYY',
                        )

fig_years = graph_years(dateInterval)
st.plotly_chart(fig_years, theme = None, use_container_width=True)