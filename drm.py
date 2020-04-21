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

import argparse
import yfinance as yf
import os
from datetime import date, timedelta

def get_data(ticker,start,end):
    cwd = os.getcwd()
    print(f"Date range is {start} to {end}")
    if not os.path.isdir("dataset/"):
        os.mkdir("dataset")
    t = yf.Ticker(ticker+".NS")
    try:
        data1 = t.history(interval="1d",start=start,end=end)
        if data1.shape[0] != 0:
            data1.to_csv(cwd+"/dataset/"+ticker+"-DAILY.csv")
            print(f'Saved to {"./dataset/"+ticker+"-DAILY.csv"}')
        data2 = t.history(interval="1wk",start=date(2019,1,1),end=date(2020,1,1))
        if data2.shape[0] != 0:
            data2.to_csv(cwd+"/dataset/"+ticker+"-WEEKLY.csv")
            print(f'Saved to {"./dataset/"+ticker+"-WEEKLY.csv"}')
        data3 = t.history(interval="1mo",start=date(2019,1,1),end=date(2020,1,1))
        if data3.shape[0] != 0:
            data3.to_csv(cwd+"/dataset/"+ticker+"-MONTHLY.csv")
            print(f'Saved to {"./dataset/"+ticker+"-MONTHLY.csv"}')
        return 0
    except:
        print("An error occured, check dates and your internet connection and please try again.")
        pass

def Main():
    parser = argparse.ArgumentParser(prog='A small client to scrape historical data from NSE website')
    parser.add_argument("symbol", help="The symbol of stock in NSE", type=str)
    parser.add_argument("year",help="The period for which data is required. Following methods work - 3d for three days, 2w for two weeks, 3m for three months and 5y for five years",type=str)
    parser.add_argument('--version', '-v', action='version', version='%(prog)s 2.0')
    args = parser.parse_args()
    print(args)
    try:
        if args.year[-1]=='y':
            get_data(args.symbol,str(date.today()-timedelta(days=int(args.year[:-1])*365)),end=date.today())
        elif args.year[-1]=='m':
            get_data(args.symbol,str(date.today()-timedelta(days=int(args.year[:-1])*30)),end=date.today())
        elif args.year[-1]=='w':
            get_data(args.symbol,str(date.today()-timedelta(days=int(args.year[:-1])*7)),end=date.today())
        elif args.year[-1]=='d':
            get_data(args.symbol,str(date.today()-timedelta(days=int(args.year[:-1]))),end=date.today())
    except ValueError:
        print("Error with period formatting, please try again")

if __name__ == "__main__":
    Main()

