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
    parser = argparse.ArgumentParser(prog='A small client to scrape historical data of stock prices from NSE website. Head over to www.github.com/animesh-srivastava/drm-scrape for more information.')
    parser.add_argument("symbol", help="The company symbol or ticker.", type=str)
    parser.add_argument("-p","--period",help="The period for which data is required. Following methods work - 3d for three days, 2w for two weeks, 3m for three months and 5y for five years.",type=str)
    parser.add_argument('--version', '-v', action='version', version='%(prog)s 2.0.1')
    parser.add_argument("-s","--start",default = str(date.today()-timedelta(days=365)),help="Specify the starting date in YYYY-MM-DD.",action='store')
    parser.add_argument("-e","--end", default=str(date.today()),help="Specify the ending date in YYYY-MM-DD.",action='store')
    args = parser.parse_args()
    if args.period and not(args.start and args.end):
        try:
            if args.period[-1]=='y':
                get_data(args.symbol, start=str(date.today()-timedelta(days=int(args.period[:-1])*365)), end=date.today())
            elif args.period[-1]=='m':
                get_data(args.symbol,start=str(date.today()-timedelta(days=int(args.period[:-1])*30)), end=date.today())
            elif args.period[-1]=='w':
                get_data(args.symbol,start=str(date.today()-timedelta(days=int(args.period[:-1])*7)), end=date.today())
            elif args.period[-1]=='d':
                get_data(args.symbol,start=str(date.today()-timedelta(days=int(args.period[:-1]))), end=date.today())
        except ValueError:
            print("Error with time period provided, please try again.")
    elif args.start and args.end and not(args.period):
        if (args.start)<=(args.end):
            get_data(args.symbol,start=args.start,end=args.end)
        else:
            print("Ending date cannot be before than starting date.")
    elif args.start and args.end and args.period:
        print("Default precedence is Date Range")
        if (args.start)<=(args.end):
            get_data(args.symbol,start=args.start,end=args.end)
        else:
            print("Ending date cannot be before than starting date.")
    elif not(args.start) and not(args.period) and not(args.end):
        print("Proceeding with default values.")
        get_data(args.symbol,start=args.start,end=args.end)
if __name__ == "__main__":
    Main()

