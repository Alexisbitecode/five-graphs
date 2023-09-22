import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {'Category': ['Math', 'English', 'P.E', 'CS', 'Science'],
        'Values': [10, 25, 15, 30, 20]}

# Create a DataFrame from the data
df = pd.DataFrame(data)
st.title("Student Counts for Each Subject")

# Create a bar plot using Matplotlib
fig, ax = plt.subplots()
ax.bar(df['Category'], df['Values'])
plt.xlabel("Subject")
plt.ylabel("Student Counts")

# Display the plot in Streamlit
st.pyplot(fig)





