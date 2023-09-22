import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

# Load data
@st.cache
def load_data():
    df = pd.read_csv("C:/Users/lwjct/Downloads/Fish.csv")
    return df

df = load_data()

# Group by species and calculate mean
group_mean = df.groupby('Species').mean()

# Display the bar chart using Streamlit
st.bar_chart(group_mean['Weight'])

# Customize the chart's appearance
st.title("The average weight for each species")
st.xlabel('Species')
st.ylabel('Average weight')


