import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import pandas as pd
import time
from sklearn.linear_model import LinearRegression
import numpy as np

# App Title
st.set_page_config(page_title="Live Stock Tracker & Prediction", page_icon="📈")
st.title('📈 Real-Time Stock Tracker + 🔮 Price Prediction')

# User input
ticker = st.text_input('Enter Stock Ticker (example: AAPL, TSLA, MSFT)', 'AAPL')

# Fetch stock data
stock = yf.Ticker(ticker)

# Display company info
st.subheader('🏢 Company Info:')
try:
    st.write(stock.info['longName'])
except:
    st.warning("Ticker not found. Please check the symbol!")

# Live Price Section
st.subheader('💹 Live Price:')

# Placeholder
price_placeholder = st.empty()
chart_placeholder = st.empty()
prediction_placeholder = st.empty()

# Initialize
prices = []
times = []
prev_price = None

# Interval input
refresh_rate = st.slider('Refresh rate (seconds)', 5, 60, 10)

# Start the live update loop
while True:
    live_data = stock.history(period='1d', interval='1m')
    current_time = pd.Timestamp.now()

    if not live_data.empty:
        last_price = live_data['Close'].iloc[-1]

        prices.append(last_price)
        times.append(current_time)

        # Compare with previous price
        if prev_price is not None:
            if last_price > prev_price:
                price_color = "🟢"
            elif last_price < prev_price:
                price_color = "🔴"
            else:
                price_color = "⚪"
        else:
            price_color = "⚪"

        prev_price = last_price

        # Show price
        price_placeholder.metric(label="Current Price", value=f"${last_price:.2f}", delta_color="inverse")

        # Draw Actual Live Chart
        fig_live = go.Figure()
        fig_live.add_trace(go.Scatter(x=times, y=prices, mode='lines+markers', name='Actual Price'))
        fig_live.update_layout(title=f"Live {ticker} Price Movement {price_color}",
                               xaxis_title="Time",
                               yaxis_title="Price (USD)",
                               template="plotly_dark",
                               showlegend=True)
        chart_placeholder.plotly_chart(fig_live, use_container_width=True)

        # Train a simple model if enough data
        if len(prices) > 10:
            st.subheader('🔮 Predicted vs Actual Price Chart')

            # Prepare data
            X = np.arange(len(prices)).reshape(-1, 1)
            y = np.array(prices)

            model = LinearRegression()
            model.fit(X, y)

            # Predict future points
            future_steps = 10
            X_future = np.arange(len(prices) + future_steps).reshape(-1, 1)
            y_pred = model.predict(X_future)

            # Actual + Predicted Line Chart
            fig_pred = go.Figure()

            # Actual prices
            fig_pred.add_trace(go.Scatter(
                x=list(range(len(prices))),
                y=prices,
                mode='lines+markers',
                name='Actual Price'
            ))

            # Predicted prices
            fig_pred.add_trace(go.Scatter(
                x=list(range(len(y_pred))),
                y=y_pred,
                mode='lines+markers',
                name='Predicted Price',
                line=dict(dash='dot')
            ))

            fig_pred.update_layout(title=f"{ticker} Price Prediction",
                                   xaxis_title="Time (minutes)",
                                   yaxis_title="Price (USD)",
                                   template="plotly_white",
                                   showlegend=True)

            prediction_placeholder.plotly_chart(fig_pred, use_container_width=True)

    time.sleep(refresh_rate)
