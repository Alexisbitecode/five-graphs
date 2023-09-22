import streamlit as st
import pandas as pd



# Define the data
data = {'Category': ['Math', 'English', 'P.E', 'CS', 'Science'],
        'Values': [10, 25, 15, 30, 20]}

# Create a DataFrame from the data
df = pd.DataFrame(data)
st.title("Student Counts for Each Subject")

# Set labels for x-axis and y-axis using Markdown
st.markdown("**X-axis Label**: Subject")
st.markdown("**Y-axis Label**: Students Counts")

# Create a bar plot using st.pyplot
st.bar_chart(df.set_index('Category')['Values'], use_container_width=True,x= "Subject", y = "Students Counts")



