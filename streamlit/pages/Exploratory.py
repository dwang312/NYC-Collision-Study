import logging

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def load_data(fp):
    df = pd.read_csv(fp)
    return df

#Data File Paths
crashesRaw = "../data/Motor_Vehicle_Collisions_-_Crashes_20231202.csv"
peopleRaw = "../data/Motor_Vehicle_Collisions_-_Person_20231202.csv"
vehiclesRaw = "../data/Motor_Vehicle_Collisions_-_Vehicles_20231202.csv"

def top_states(df):
    stateRegistered = pd.DataFrame(df['STATE_REGISTRATION' ].value_counts()).reset_index()
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

    return fig, stateList[0:10]

#exploratory questions
questions = {
    'What is the distribution of crashes by contributing factor?' : 1,
    'What is the distribution of crashes by vehicle type?' : 2,
    'What is the distribution of crashes by borough?' : 3,
    'Which out of state vehicles are involved in the most crashes?':4,
}

option = st.selectbox('Select exploratory question:',[q for q in questions.keys()])

if questions[option] == 1:
    logging.info("Plotting contributing factor")
elif questions[option] == 2:
    logging.info("Plotting vehicle type distribution")
elif questions[option] == 3:
    logging.info("Plotting borough distribution")
elif questions[option] == 4:
    logging.info("Plotting top states")
    df_vehicle = load_data(vehiclesRaw)
    fig, table = top_states(df_vehicle)
    st.pyplot(fig)
    #st.dataframe(table)
    st.markdown(table.to_markdown())
