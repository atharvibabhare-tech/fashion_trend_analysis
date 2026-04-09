import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Fashion Dashboard", layout="wide")

st.title("👗 Fashion Trends Analysis Dashboard")

# -----------------------------
# 🔹 LOAD DATA
# -----------------------------
try:
    df = pd.read_csv("Fashion_Trends.csv")
except:
    st.error("❌ File not found. Please keep CSV in same folder.")
    st.stop()

# -----------------------------
# 🔹 DATA CLEANING
# -----------------------------
df['Original_Price'] = pd.to_numeric(df['Original_Price'], errors='coerce')

# -----------------------------
# 🔹 SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("🔍 Filter Data")

# Category filter
category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + sorted(df['Category'].dropna().unique())
)

# Brand filter
brand = st.sidebar.selectbox(
    "Select Brand",
    ["All"] + sorted(df['Brand'].dropna().unique())
)

# Product search (better than dropdown)
product_search = st.sidebar.text_input("🔎 Search Product")

# -----------------------------
# 🔹 APPLY FILTERS
# -----------------------------
filtered_df = df.copy()

if category != "All":
    filtered_df = filtered_df[filtered_df['Category'] == category]

if brand != "All":
    filtered_df = filtered_df[filtered_df['Brand'] == brand]

if product_search:
    filtered_df = filtered_df[
        filtered_df['Product_Name'].str.contains(product_search, case=False, na=False)
    ]

# -----------------------------
# 🔹 HANDLE EMPTY DATA
# -----------------------------
if filtered_df.empty:
    st.warning("⚠️ No data available for selected filters")
    st.stop()

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
ax3.set_title("Category Distribution")
st.pyplot(fig3)

# -----------------------------
# 🔹 GRAPH 4: TOP BRANDS
# -----------------------------
st.write("### 📊 Top Brands")

fig4, ax4 = plt.subplots()
filtered_df['Brand'].value_counts().head(10).plot(kind='bar', ax=ax4)
ax4.set_title("Top 10 Brands")
st.pyplot(fig4)

# -----------------------------
# 🔹 GRAPH 5: PRICE SEGMENT PIE
# -----------------------------
if 'Price_Segment' in filtered_df.columns:
    st.write("### 💰 Price Segment Distribution")

    fig5, ax5 = plt.subplots()
    filtered_df['Price_Segment'].value_counts().plot(
        kind='pie',
        autopct='%1.1f%%',
        ax=ax5
    )
    ax5.set_ylabel("")
    st.pyplot(fig5)

# -----------------------------
# 🔹 FOOTER
# -----------------------------
st.markdown("---")
st.markdown("✨ Created by Atharvi | Fashion Data Analysis Project")
