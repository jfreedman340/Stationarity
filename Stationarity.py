'''
This is the Augmented Dickey-Fuller Test using the adfuller module from statsmodels, 
and it tells me whether or not data is stationary. I wrote this program based on a lesson 
from my Financial Engineering and Artificial Intelligence course on Udemy by LazyProgrammer.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import random
from statsmodels.tsa.stattools import adfuller

#Getting stock price data.
stocks = pd.read_csv('sp500sub.csv', index_col='Date', parse_dates=True)
ticker = input("Enter a ticker symbol: ")

stock = stocks[stocks['Name'] == f'{ticker}'][['Close']]
stock['LogPrice'] = np.log(stock['Close'])
stock['LogRet'] = stock['LogPrice'].diff()

#The Augmented Dickey-Fuller Test. Show whether or not the data is stationary.
def adf(x):
  res = adfuller(x)
  print("Test-Statistic:", res[0])
  print("P-Value:", res[1])
  if res[1] < 0.05:
    print("Stationary")
  else:
    print("Non-Stationary")

#Show the results.
print(f'ADF Test for {ticker} price:')
print(adf(stock['LogPrice']))
print(f'ADF Test for {ticker} returns:')
print(adf(stock['LogRet'].dropna()))