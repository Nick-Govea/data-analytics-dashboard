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
st.line_chart(data)
st.write(data)

