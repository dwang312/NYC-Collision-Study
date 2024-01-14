import logging

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


st.set_page_config(layout="wide")

@st.cache_data

def load_data(fp):
    df = pd.read_csv(fp, low_memory=False)
    return df

#Data File Paths
crashesRaw = "../data/Motor_Vehicle_Collisions_-_Crashes_20231202.csv"
peopleRaw = "../data/Motor_Vehicle_Collisions_-_Person_20231202.csv"
vehiclesRaw = "../data/Motor_Vehicle_Collisions_-_Vehicles_20231202.csv"

def contributing_factor():
    df_collisions = load_data(crashesRaw)
    #create a new data frame containing vehicle 1 type accident cause and the the number of accidents caused
    df_NYaccidentcause=pd.DataFrame(df_collisions['CONTRIBUTING FACTOR VEHICLE 1'].value_counts()) 
    top10accidentcauses=pd.Series(df_NYaccidentcause.head(10).index)
    top10C=df_collisions[df_collisions['CONTRIBUTING FACTOR VEHICLE 1'].isin(top10accidentcauses)]

    topCFactors=pd.DataFrame(top10C.groupby(['BOROUGH','CONTRIBUTING FACTOR VEHICLE 1']).size(), columns=['count'])
    topCFactors.reset_index(inplace=True)
    topCFactors=topCFactors.pivot(index='BOROUGH',columns='CONTRIBUTING FACTOR VEHICLE 1',values='count')

    #drop the unspecified entry
    topCFactors.drop(['Unspecified'],axis=1,inplace=True)

    fig, axes = plt.subplots(1,1,figsize=(13,8))
    ax = topCFactors.plot(ax=axes,kind='bar', stacked=True)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0, horizontalalignment='right', ha='center')

    ax.set_xlabel('Borough', weight ='bold')
    ax.set_ylabel('Number of Accidents', weight ='bold')
    ax.set_title('Top 9 Accident Causes by Borough (July 2012 - Present)', weight='bold', fontsize=16)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1))

    return fig

def top_states():
    df_vehicle = load_data(vehiclesRaw)
    stateRegistered = pd.DataFrame(df_vehicle['STATE_REGISTRATION' ].value_counts()).reset_index()
    c1 = stateRegistered['STATE_REGISTRATION'] != 'NY'
    stateList = stateRegistered[c1]
    fig = plt.figure(figsize=(34,21))
    ax = sns.barplot(data = stateList[0:10], x = 'STATE_REGISTRATION', y = 'count',
                    hue = 'STATE_REGISTRATION',
                    palette = "tab10")
    ax.set_title('Top 10 Vehicle State Registeration (excluding NY) involved in a Collision', fontsize = 30)
    ax.set_xlabel('Origin State', fontsize = 20)
    ax.set_ylabel('Number of Vehicles', fontsize = 20)

    for i in ax.containers:
        ax.bar_label(i,)
    stateList.rename(columns = {'STATE_REGISTRATION':'State', 'count':'Collision Count'}, inplace = True)
    return fig, stateList[0:10]

def florida_roadways():
    df_crashes = load_data(crashesRaw)
    df_vehicle = load_data(vehiclesRaw)
    df = pd.merge(df_vehicle, df_crashes[['COLLISION_ID','ON STREET NAME']], on='COLLISION_ID', how='left')
    df.dropna(subset=['ON STREET NAME'], inplace=True)
    df_florida = df[df['STATE_REGISTRATION'] == 'FL']
    df_florida['ON STREET NAME'].value_counts().head(10)
    florida_count = pd.DataFrame(df_florida['ON STREET NAME'].value_counts()).reset_index()

    # Your data setup and bar plot code
    fig = plt.figure(figsize=(21,13))
    ax = sns.barplot(x='count', y='ON STREET NAME', data=florida_count.head(10), palette='viridis', hue='ON STREET NAME')

    # Get the bars sorted by count in descending order
    sorted_bars = sorted(ax.patches, key=lambda x: x.get_width(), reverse=True)

    # Get the highest bar
    highest_bar = sorted_bars[0]

    # Create a custom color list
    custom_colors = ['lightgray'] * len(sorted_bars)  # Set default color for all bars

    # Assign the same color from Viridis palette for the 2nd, 3rd, and 4th bars after the highest
    color_for_234 = sns.color_palette('viridis')[1]  # Replace '5' with the index of the desired color from Viridis palette
    for i in range(len(sorted_bars)):
        if i in range(sorted_bars.index(highest_bar) + 1, sorted_bars.index(highest_bar) + 4):  # Set colors for the 2nd, 3rd, and 4th bars after the highest
            custom_colors[i] = color_for_234  # Set the same color for the bars

    # Set color for the highest bar
    custom_colors[0] = sns.color_palette('viridis')[0]  # Set color for the highest bar

    # Assign colors to bars
    for i, bar in enumerate(sorted_bars):
        bar.set_facecolor(custom_colors[i])

    # Set title, labels, and bar labels if needed
    ax.set_title('Top 10 Streets with Florida Registered Vehicles (2016-2023)')
    ax.set_xlabel('Number of Vehicles Involved In A Collision')
    ax.set_ylabel('Roadway Name')

    for i in ax.containers:
        ax.bar_label(i)

    return fig

#exploratory questions
questions = {
    'What is the distribution of crashes by contributing factor?' : 1,
    'What is the distribution of crashes by vehicle type?' : 2,
    'What is the distribution of crashes by borough?' : 3,
    'Which out of state vehicles are involved in the most crashes?': 4,
    'Where are Flordian vehicles involved in the most crashes?': 5,
}

option = st.selectbox('Select exploratory question:',[q for q in questions.keys()])

col1, col2 = st.columns([1,4])
if questions[option] == 1:
    logging.info("Plotting contributing factor")
    fig = contributing_factor()
    st.pyplot(fig)
elif questions[option] == 2:
    logging.info("Plotting vehicle type distribution")
elif questions[option] == 3:
    logging.info("Plotting borough distribution")
elif questions[option] == 4:
    logging.info("Plotting top states")
    fig, table = top_states()
    st.pyplot(fig)
    st.markdown(table.to_markdown())
elif questions[option] == 5:
    logging.info("Plotting Florida")
    with col1:
        st.write("Temp")
    with col2:
        fig = florida_roadways()
        st.pyplot(fig)

