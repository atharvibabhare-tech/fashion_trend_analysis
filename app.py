import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("👗 Fashion Trends Analysis")

df = pd.read_csv("Fashion_Trends.csv")

st.write("### Dataset Preview")
st.dataframe(df.head())

# Example Graph
st.write("### Price Distribution")
fig, ax = plt.subplots()
df['Original_Price'].plot(kind='hist', ax=ax)
st.pyplot(fig)

# Pie Chart
st.write("### Discount Distribution")
discount_counts = df['Discount_Tier'].value_counts()

fig2, ax2 = plt.subplots()
discount_counts.plot(kind='pie', autopct='%1.1f%%', ax=ax2)
ax2.set_ylabel("")
st.pyplot(fig2)
