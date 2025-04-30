import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("buffett_holdings.csv")

# Data preprocessing
df['Shares'] = df['Shares'].str.replace(',', '').astype(float)
df['Change Numeric'] = df['Change Numeric'].astype(float)

# Expanded sector mapping
sector_map = {
    'AAPL - Apple Inc.': 'Technology',
    'AXP - American Express': 'Financial Services',
    'BAC - Bank of America Corp.': 'Financial Services',
    'KO - Coca Cola Co.': 'Consumer Goods',
    'CVX - Chevron Corp.': 'Energy',
    'OXY - Occidental Petroleum': 'Energy',
    'MCO - Moody\'s Corp.': 'Financial Services',
    'KHC - Kraft Heinz Co.': 'Consumer Goods',
    'DVA - DaVita HealthCare Partners': 'Healthcare',
    'AMZN - Amazon.com Inc.': 'Technology',
    'MA - Mastercard Inc.': 'Financial Services',
    'V - Visa Inc.': 'Financial Services',
    'ALLY - Ally Financial Inc.': 'Financial Services'
}

df['Sector'] = df['Stock'].map(sector_map)

st.set_page_config(page_title="Buffett Holdings Dashboard", layout="wide")

st.title("Warren Buffett Portfolio Analysis Dashboard")

# Sidebar filters
st.sidebar.header("Filters")
selected_sector = st.sidebar.selectbox("Select Sector", ['All'] + list(df['Sector'].unique()))
min_change = st.sidebar.slider("Minimum % Change", -50.0, 50.0, (-50.0, 50.0))

# Apply filters
filtered_df = df.copy()
if selected_sector != 'All':
    filtered_df = filtered_df[filtered_df['Sector'] == selected_sector]
filtered_df = filtered_df[(filtered_df['Change Numeric'] >= min_change[0]) & 
                         (filtered_df['Change Numeric'] <= min_change[1])]

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["Portfolio Overview", "Performance Analysis", "Risk & Sector Exposure", "New Insights"])

with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Top 10 Holdings by Value")
        top_holdings = filtered_df.sort_values('Value', ascending=False).head(10)
        fig = px.bar(top_holdings, x='Value', y='Stock', orientation='h',
                     title="Top Holdings by Market Value")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Sector Allocation")
        sector_allocation = filtered_df.groupby('Sector')['Value'].sum().reset_index()
        fig = px.pie(sector_allocation, values='Value', names='Sector', 
                     title="Portfolio Value by Sector")
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Top Gainers")
        gainers = filtered_df[filtered_df['Change Numeric'] > 0].sort_values('Change Numeric', ascending=False).head(5)
        st.dataframe(gainers[['Stock', 'Change Numeric']].style.format({'Change Numeric': '{:.2f}%'}))

    with col2:
        st.subheader("Top Losers")
        losers = filtered_df[filtered_df['Change Numeric'] < 0].sort_values('Change Numeric').head(5)
        st.dataframe(losers[['Stock', 'Change Numeric']].style.format({'Change Numeric': '{:.2f}%'}))

    st.subheader("Price Comparison")
    fig = px.line(filtered_df, x='Stock', y=['Reported Price', 'Recent Price'],
                 title="Reported vs Recent Prices")
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Risk Exposure")
        risk_exposure = filtered_df.sort_values('Risk Impact', ascending=False).head(10)
        fig = px.bar(risk_exposure, x='Risk Impact', y='Stock', orientation='h',
                    title="Stocks with Highest Risk Impact")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Concentration Analysis")
        hhi = (filtered_df['weight']**2).sum()
        st.metric("Herfindahl Index", f"{hhi:.4f}")
        st.caption("Lower values indicate more diversification")

with tab4:
    st.subheader("New Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Correlation Matrix**")
        numeric_cols = filtered_df[['Reported Price', 'Recent Price', 'Value', 'Change Numeric']]
        fig = px.imshow(numeric_cols.corr(), text_auto=True)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("**Shares Distribution**")
        fig = px.histogram(filtered_df, x='Shares', nbins=20, 
                          title="Distribution of Shares Held")
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("**Sector Performance Analysis**")
    sector_perf = filtered_df.groupby('Sector').agg({'Change Numeric':'mean', 'Value':'sum'}).reset_index()
    fig = px.scatter(sector_perf, x='Change Numeric', y='Value', size='Value', color='Sector',
                    labels={'Change Numeric':'Average % Change', 'Value':'Total Value'},
                    title="Sector Performance Overview")
    st.plotly_chart(fig, use_container_width=True)

st.sidebar.markdown("---")
st.sidebar.download_button("Download Filtered Data", filtered_df.to_csv(), "filtered_holdings.csv")