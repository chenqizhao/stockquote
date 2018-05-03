
# coding: utf-8

# In[ ]:


from pandas_datareader.nasdaq_trader import get_nasdaq_symbols
import requests
def getName(ticker):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(ticker)
    count = 0
    try:
        result = requests.get(url).json()
        for x in result['ResultSet']['Result']:
            if x['symbol'] == ticker:
                company =  x['name']
                count += 1
    except KeyError:
        print("Oops!  Something wrong with your input ticker  Try again...")
        return
    try:
        assert count == 1
    except AssertionError:
        print("Oops!  Something wrong with your input ticker  Try again...")
        return
    return company
import pandas as pd
import pandas_datareader.data as web   # Package and modules for importing data; this code may change depending on pandas version
import time
import datetime
from datetime import date, timedelta
from pandas_datareader import data as wb

def getPrice(ticker):
    start = datetime.date.today()
    end = datetime.date.today()
    current_time = time.strftime("%c") + " " + time.strftime("%Z")
    yesterday = date.today() - timedelta(1)
    company_name = getName(str(ticker))
    try:
        assert company_name != None
    except AssertionError:
        print("Oops!  Something wrong with your input ticker  Try again...")
        return
    print(company_name + " (" + ticker + ")")
    print(current_time)
    try:
        df = wb.DataReader(ticker, 'morningstar', start, end)
    except TypeError:
        print("Oops!  No transaction for your ticker today. Try again with previous dates OR try again later")
        return
    try:
        open_price = df.iloc[-1]['Open']
        close_price = df.iloc[-1]['Close']
    except JSONDecodeError:
        print("Oops!  No transaction for your ticker today. Try again with previous dates OR try again later")
        return
        
    benefit = close_price - open_price
    percent = benefit / open_price
    if benefit >= 0.00:
        benefit = "%.2f" % benefit
        income = "+" + benefit
    elif benefit < 0:
        benefit = "%.2f" % benefit
        income = benefit
    percent = percent * 100
    if percent >= 0.00:
        percent = "%.2f" % percent
        percent = "+" + percent
    elif percent < 0.00:
        percent = "%.2f" % percent
    output = str(close_price) + " " + income + " (" + percent + "%" + ")"
    print(output)
    ticker = ""

if __name__ == "__main__":
    while True:
        stockname = input("Please enter stalk symbol: ")
        ticker = stockname.split(":")[0]
        getPrice(ticker)

