import pandas as pd
import numpy as np
import streamlit  as st
import math


data = pd.read_csv("data.csv")
data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%y', errors='coerce')
data = data.set_index('Date')
#Title
st.title("Personal Data Tracker")
#Shows the Data

#Sleep Score
st.subheader("Sleep Score")
st.line_chart(data['Sleep Score'])

#Deep Sleep Score
st.subheader("Deep Sleep Score")
st.line_chart(data['Deep Sleep Score'])

#Hours Slept
st.subheader("Hours Slept")
st.line_chart(data['Hours Slept'])

#Calories
st.subheader("Calories")
st.bar_chart(data['Calories'])

#Weight
st.subheader("Weight")
st.line_chart(data['Weight'])

#Mood
st.subheader("Mood")
st.line_chart(data['Mood'])

