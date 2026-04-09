import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("👗 Fashion Trends Analysis")

# Load Data
df = pd.read_csv("Fashion_Trends.csv")

# Clean numeric
df['Original_Price'] = pd.to_numeric(df['Original_Price'], errors='coerce')

# -----------------------------
# 🔹 FILTER SECTION
# -----------------------------
st.sidebar.header("🔍 Filter Data")

category = st.sidebar.selectbox("Select Category", ["All"] + list(df['Category'].dropna().unique()))
brand = st.sidebar.selectbox("Select Brand", ["All"] + list(df['Brand'].dropna().unique()))
product = st.sidebar.selectbox("Select Product", ["All"] + list(df['Product_Name'].dropna().unique()))

# Apply filters
filtered_df = df.copy()

if category != "All":
    filtered_df = filtered_df[filtered_df['Category'] == category]

if brand != "All":
    filtered_df = filtered_df[filtered_df['Brand'] == brand]

if product != "All":
    filtered_df = filtered_df[filtered_df['Product_Name'] == product]

# -----------------------------
# 🔹 DATA PREVIEW
# -----------------------------
st.write("### 📄 Filtered Dataset")
st.dataframe(filtered_df.head())

# -----------------------------
# 🔹 GRAPH 1: PRICE DISTRIBUTION
# -----------------------------
st.write("### 📊 Price Distribution")

fig, ax = plt.subplots()
filtered_df['Original_Price'].dropna().plot(kind='hist', ax=ax)
ax.set_title("Original Price Distribution")
st.pyplot(fig)

# -----------------------------
# 🔹 GRAPH 2: DISCOUNT PIE
# -----------------------------
st.write("### 🥧 Discount Distribution")

discount_counts = filtered_df['Discount_Tier'].value_counts()

fig2, ax2 = plt.subplots()
discount_counts.plot(kind='pie', autopct='%1.1f%%', ax=ax2)
ax2.set_ylabel("")
st.pyplot(fig2)

# -----------------------------
# 🔹 GRAPH 3: CATEGORY BAR
# -----------------------------
st.write("### 📊 Category Distribution")

fig3, ax3 = plt.subplots()
filtered_df['Category'].value_counts().plot(kind='bar', ax=ax3)
st.pyplot(fig3)

# -----------------------------
# 🔹 GRAPH 4: BRAND BAR
# -----------------------------
st.write("### 📊 Top Brands")

fig4, ax4 = plt.subplots()
filtered_df['Brand'].value_counts().head(10).plot(kind='bar', ax=ax4)
st.pyplot(fig4)
