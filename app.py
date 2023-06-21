import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.express as px
import yfinance as yf
import streamlit as st

def plot_stock_momentum(stock_ticker, period):
    # Get stock data from Yahoo Finance
    stock = yf.Ticker(stock_ticker)
    data = stock.history(period=period)

    # Calculation of momentum
    data['momentum'] = data['Close'].pct_change()

    # Creating subplots to show momentum and buying/selling markers
    figure = make_subplots(rows=2, cols=1)
    figure.add_trace(go.Scatter(x=data.index, 
                             y=data['Close'], 
                             name='Close Price'))
    figure.add_trace(go.Scatter(x=data.index, 
                             y=data['momentum'], 
                             name='Momentum', 
                             yaxis='y2'))

    # Adding the buy and sell signals
    figure.add_trace(go.Scatter(x=data.loc[data['momentum'] > 0].index, 
                             y=data.loc[data['momentum'] > 0]['Close'], 
                             mode='markers', name='Buy', 
                             marker=dict(color='green', symbol='triangle-up')))

    figure.add_trace(go.Scatter(x=data.loc[data['momentum'] < 0].index, 
                             y=data.loc[data['momentum'] < 0]['Close'], 
                             mode='markers', name='Sell', 
                             marker=dict(color='red', symbol='triangle-down')))

    figure.update_layout(title='Algorithmic Trading using Momentum Strategy',
                      xaxis_title='Date',
                      yaxis_title='Price')
    figure.update_yaxes(title="Momentum", secondary_y=True)
    st.plotly_chart(figure)

def main():
    st.title('Algorithmic Trading')
    stock_ticker = st.text_input('Enter a stock ticker (e.g., AAPL)')
    period = st.selectbox('Select a period', ['1mo', '3mo', '6mo', '1y'])

    if stock_ticker:
        try:
            plot_stock_momentum(stock_ticker, period)
        except Exception as e:
            st.error('Error: {}'.format(str(e)))

if __name__ == '__main__':
    main()


