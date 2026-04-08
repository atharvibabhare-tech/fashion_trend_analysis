#  Fashion Trends Analysis

##  Project Overview
This project focuses on analyzing fashion product data to understand trends in pricing, discounts, brands, and categories. The goal is to extract meaningful insights that help in understanding customer preferences and market strategies.

---

##  Objectives
- Analyze distribution of products across price segments  
- Understand discount patterns and strategies  
- Identify top brands and popular categories  
- Explore relationship between price and discounts  
- Generate insights for better business decisions  

---

##  Dataset Description
The dataset contains information about fashion products with the following key columns:

- **Brand** – Name of the brand  
- **Category** – Type of product (Topwear, Footwear, etc.)  
- **Gender** – Target audience  
- **Original_Price** – Actual price  
- **Discount_Price** – Selling price  
- **Discount_Percentage** – Discount offered  
- **Price_Segment** – Budget, Mid, Premium  
- **Discount_Tier** – Low, Moderate, Deep  

---

## Data Cleaning
- Removed missing values and duplicates  
- Converted price columns to numeric format  
- Cleaned text columns (Brand, Category, Gender)  
- Created new features:
  - Discounted Amount  
  - Discount Percentage  
  - Price Segments  
  - Discount Tiers  

---

## Exploratory Data Analysis (EDA)

### 🔹 Key Visualizations
- Price Distribution (Histogram)  
- Discount Distribution (Histogram)  
- Category-wise Product Count (Bar Chart)  
- Brand-wise Analysis (Bar Chart)  
- Price vs Discount (Scatter Plot)  
- Price Segment Distribution (Pie Chart)  
- Discount Tier Distribution (Pie Chart)  
- Category vs Price Segment (Stacked Bar Chart)  
- Brand vs Price Segment (Stacked Bar Chart)  

---

##  Key Insights

- Most products fall in the **budget and mid-range price segments**  
- **Topwear and Westernwear** dominate the dataset  
- Brands prefer offering **moderate to deep discounts**  
- **Luxury products are very limited**  
- Few brands like Ajio have **strong presence across segments**  
- Discounts are not always proportional to price  

---

##  Conclusion
The analysis shows that the fashion market is largely focused on affordable products with competitive pricing strategies. Brands emphasize discounts and popular categories to attract customers, while premium and luxury segments remain limited.

---

##  Tools & Technologies Used
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Streamlit  

---

##  Project Features
- Data Cleaning & Preprocessing  
- Exploratory Data Analysis  
- Visual Insights  
- Interactive Dashboard (Streamlit)  

---

##  Deployment
This project is deployed using Streamlit for interactive visualization.

---

## 📁 Project Structure
