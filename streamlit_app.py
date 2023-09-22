import streamlit as st
import pandas as pd



# Define the data
data = {'Category': ['A', 'B', 'C', 'D', 'E'],
        'Values': [10, 25, 15, 30, 20]}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Create a bar plot using st.pyplot
st.bar_chart(df.set_index('Category')['Values'], use_container_width=True)



