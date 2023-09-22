iimport streamlit as st
import pandas as pd

# Load the data from a CSV file
df = pd.read_csv("fish.csv")

# Create a scatter plot using Streamlit
st.scatter_chart(df[['Weight', 'Height']], use_container_width=True, width=0, height=0)

