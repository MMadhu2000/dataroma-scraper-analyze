# Dataroma Scraper & Analysis

This project scrapes Warren Buffett's portfolio from [Dataroma](https://www.dataroma.com/m/holdings.php?m=BRK), stores the data in JSON, and allows further analysis.

## Features

- Scrapes stock holdings: stock name, shares, prices, etc.
- Saves as `buffett_holdings.json`
- Easy to expand with analysis or visualization tools
  
# Warren Buffett Portfolio Analysis Dashboard

![Dashboard Screenshot]![image](https://github.com/user-attachments/assets/6db26771-c255-4417-aaca-5e42a676991e)
 <!-- Add your screenshot here -->

## 📖 Overview
Interactive Streamlit dashboard analyzing Warren Buffett's stock holdings through various visualizations and metrics. Provides insights into portfolio composition, performance trends, risk exposure, and sector allocation.

## ✨ Key Features
- **Portfolio Overview**: 
  - Top 10 holdings by market value
  - Sector allocation pie chart
- **Performance Analysis**:
  - Top gainers/losers table
  - Price comparison trends
- **Risk & Sector Exposure**:
  - Risk impact visualization
  - Diversification metrics (Herfindahl Index)
- **New Insights**:
  - Correlation matrix of key metrics
  - Shares distribution analysis
  - Sector performance bubble chart
- **Interactive Filters**:
  - Sector selection
  - Price change range slider
  - Data export capability

## 🛠️ Installation
1. **Clone repository**
   ```bash
   git clone https://github.com/yourusername/buffett-dashboard.git
   cd buffett-dashboard
Install dependencies

bash
pip install -r requirements.txt
Data Preparation
Ensure buffett_holdings.csv is in the project root directory

Run dashboard

bash
streamlit run dashboard.py
📊 Usage
Sidebar Controls
Filters Screenshot ![image](https://github.com/user-attachments/assets/5009ae0c-2255-4421-a9dc-e1f8adc85ce4)

💡 Features
✅ User Controls
Select sectors from the dropdown menu

Adjust % change range using the interactive slider

🧭 Tab Navigation
Easily switch between four key analysis sections:

Portfolio Overview

Performance Analysis

Risk & Sector Exposure

New Insights

📊 Interactive Elements
Hover over charts to view detailed values

Click legend items to toggle data visibility

Use plot controls to zoom and pan across visualizations

📸 Screenshots

Portfolio Overview
![image](https://github.com/user-attachments/assets/0b37d84a-f493-4fcc-afbf-14393962c6d9)

Portfolio View
![image](https://github.com/user-attachments/assets/4cf27770-3f14-47d9-8e91-4a42e85f135c)

Performance Analysis
![image](https://github.com/user-attachments/assets/545e7dc5-be97-4782-93d6-c390c4b81427)

Price Comparision
![image](https://github.com/user-attachments/assets/ffc00781-34b9-4f1a-b493-70cee5dfd25f)


Risk & Sector Exposure
![image](https://github.com/user-attachments/assets/2dc7eed0-a470-4031-9575-e74acd3cb36c)

!New Insights
Correlation Matrix
![image](https://github.com/user-attachments/assets/83530e3c-da4b-410c-b1f8-3de5ec15cf7f)

Share Distribution
![image](https://github.com/user-attachments/assets/532058ed-926a-463d-b590-19d77fa4bd41)

Sector Performance Analysis
![image](https://github.com/user-attachments/assets/35551205-aed7-413a-9caf-e1afaa150129)

📦 Dependencies
Python 3.8+

Streamlit

Pandas

Plotly

Matplotlib

📈 Data Sources
Portfolio data: buffett_holdings.csv

Sector classifications: Custom mapping

Pricing data: Latest market values

🚀 Future Enhancements
Add historical performance tracking

Compare against S&P 500 index

Dividend yield analysis

News sentiment integration

Portfolio simulation tool

📄 License
MIT License - See LICENSE

🤝 Contributing
Fork repository

Create feature branch

Submit PR with detailed description

Report issues using template

Note: Requires Python environment setup. Contact maintainer for data sourcing questions.
