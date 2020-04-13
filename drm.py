# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:08:57 2020

@author: animesh-srivastava
"""

'''
before running the script, install yfinance and pandas in your laptop by using the following commands
!pip install yfinance
!pip install pandas
!pip install lxml
You can also run this code in Google Colab (although that would be an overkill)
'''

#%%
import sys
import yfinance as yf
import pandas as pd
import os
from datetime import date
#%%

cwd = os.getcwd()

tickers = sys.argv[1]
if not os.path.isdir("dataset/"):
     os.mkdir("dataset")
t = yf.Ticker(tickers+".NS")
try:
    data = t.history(interval="1d",start=date(2019,1,1),end=date(2020,1,1))
    data.to_csv(cwd+"/dataset/"+tickers+"-DAILY.csv")
    print(f'Saved to {cwd+"/dataset/"+tickers+"-DAILY.csv"}')
    data = t.history(interval="1wk",start=date(2019,1,1),end=date(2020,1,1))
    data.to_csv(cwd+"/dataset/"+tickers+"-WEEKLY.csv")
    print(f'Saved to {cwd+"/dataset/"+tickers+"-WEEKLY.csv"}')
    data = t.history(interval="1mo",start=date(2019,1,1),end=date(2020,1,1))
    data.to_csv(cwd+"/dataset/"+tickers+"-MONTHLY.csv")
    print(f'Saved to {cwd+"/dataset/"+tickers+"-MONTHLY.csv"}')
except urllib2.HTTPError:
    print("Not connected to internet, please try again."
