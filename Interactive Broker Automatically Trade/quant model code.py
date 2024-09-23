# Necessary imports
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import Order
import threading
import time
import pandas as pd
import numpy as np
import datetime as dt
from datetime import timedelta
from pandas import DateOffset

# Define the list of 30 stocks (assuming these are the tickers)
stocks_list = [
    'AAPL', 'MSFT', 'GOOGL', 'FB', 'AMZN',
    'NFLX', 'TSLA', 'BRK-B', 'V', 'JNJ',
    'WMT', 'PG', 'DIS', 'MA', 'NVDA',
    'HD', 'PYPL', 'BAC', 'VZ', 'ADBE',
    'CMCSA', 'KO', 'NKE', 'MRK', 'PFE',
    'T', 'PEP', 'INTC', 'CSCO', 'XOM'
]

# Initialize a DataFrame to store the signals for each stock
signals_df = pd.DataFrame(columns=['Stock', 'Signal', 'Rank'])


!pip install yfinance
!pip install requests

import yfinance as yf
import requests
import pandas as pd

ALPHA_VANTAGE_API_KEY = 'CBQP7WV5FD1RT1A2'

# get financial data from Alpha Vantage
def get_financial_data(symbol, api_key=ALPHA_VANTAGE_API_KEY):
    url = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={symbol}&apikey={api_key}'
    r = requests.get(url)
    data = r.json()
    try:
        latest_annual_report = data['annualReports'][0]
        total_assets = float(latest_annual_report['totalAssets'])
        total_liabilities = float(latest_annual_report['totalLiabilities'])
        book_value = total_assets - total_liabilities
        return book_value
    except Exception as e:
        print(f"Error fetching financial data for {symbol}: {e}")
        return None

# iterate all stocks
results = []

for ticker_symbol in stocks_list:
    stock = yf.Ticker(ticker_symbol)
    try:
        market_data = stock.history(period="1d")
        market_cap = market_data['Close'].iloc[-1] * stock.info['sharesOutstanding']
        book_value = get_financial_data(ticker_symbol)
        if book_value:
            book_to_market_ratio = book_value / market_cap
            results.append({
                'Ticker': ticker_symbol,
                'Market Cap': market_cap,
                'Book Value': book_value,
                'Book-to-Market Ratio': book_to_market_ratio
            })
    except Exception as e:
        print(f"Error processing {ticker_symbol}: {e}")

# save the results as df
results_df = pd.DataFrame(results)
print(results_df)


API_KEY = 'UJZD1DG4FEHYGHQQ'
# 查询Alpha Vantage以获取股票概览数据
def get_stock_overview(symbol, api_key):
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for {symbol}")
        return None

# 收集所有股票的概览数据
data = []
for symbol in stocks_list:
    overview_data = get_stock_overview(symbol, API_KEY)
    if overview_data:
        data.append(overview_data)

# 转换为DataFrame
df = pd.DataFrame(data)

# 选择显示部分感兴趣的列，这里可以根据需要调整
columns_list = df.columns.tolist()
columns_df = pd.DataFrame(columns_list, columns=['Column Names'])

# 选择一只股票作为示例
symbol = 'AAPL'
stock = yf.Ticker(symbol)

# 获取股票的详细信息
info = stock.info

# 将信息字典的键（列名）转换为DataFrame
columns_df = pd.DataFrame(list(info.keys()), columns=['Available Data Columns'])

# 将信息字典的键（列名）转换为列表
columns_list = list(info.keys())

# 显示所有可用的数据列名列表
print(columns_list)


import yfinance as yf
import pandas as pd

# 尝试获取标普500指数的P/E比率
sp500 = yf.Ticker("^GSPC")
sp500_info = sp500.info
sp500_pe = sp500_info.get('trailingPE')

# 如果无法获取标普500指数的P/E，使用一个固定的参考值作为示例
if sp500_pe is None:
    sp500_pe = 20  # 假设值

# 定义股票列表
stocks_list = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']

# 初始化数据集
data = {
    'Symbol': [],
    'PE_Vs_Market': [],
    'EPS_Growth': [],
    'Earnings_Momentum_3mth': [],
    'Net_Revisions_FY2_EPS': [],
    'Mean_FY2_EPS': [],
    '12Mth_Price_Momentum': [],
    '1Mth_Price_Reversion': [],
    'ROE': [],
    'Earnings_Risk': [],
    'Q_Score': []
}

# 遍历股票列表，获取数据和计算指标
for symbol in stocks_list:
    stock = yf.Ticker(symbol)
    hist = stock.history(period="1y")  # 获取历史数据

    # 计算12个月价格动量
    data['12Mth_Price_Momentum'].append(hist['Close'].iloc[-1] / hist['Close'].iloc[0] - 1)

    # 计算1个月价格反转
    data['1Mth_Price_Reversion'].append(hist['Close'].iloc[-1] / hist['Close'].iloc[-22] - 1)

    # 获取股票信息
    info = stock.info

    # 个股的P/E比率
    stock_pe = info.get('trailingPE')
    # 估算PE相对于市场的值
    if stock_pe:
        pe_vs_market = stock_pe / sp500_pe
    else:
        pe_vs_market = None
    data['PE_Vs_Market'].append(pe_vs_market)

    # 添加其他指标
    eps_growth = info.get('earningsQuarterlyGrowth')
    data['EPS_Growth'].append(eps_growth)
    data['ROE'].append(info.get('returnOnEquity'))
    data['Earnings_Risk'].append(eps_growth)  # 使用季度增长作为风险指标的近似值

    # 使用earningsQuarterlyGrowth作为盈利动量的替代指标
    data['Earnings_Momentum_3mth'].append(eps_growth)

    # 假设FY2 EPS增长为earningsQuarterlyGrowth的一部分
    fy2_eps_growth = eps_growth if eps_growth is not None else 0
    last_quarter_growth = info.get('lastQuarterEarningsGrowth', 0)
    net_revisions_fy2_eps = fy2_eps_growth - last_quarter_growth
    data['Net_Revisions_FY2_EPS'].append(net_revisions_fy2_eps)

    # 假设Mean FY2 EPS
    data['Mean_FY2_EPS'].append(fy2_eps_growth)

    # 添加股票符号
    data['Symbol'].append(symbol)

    # 计算Q得分（这里使用简化的权重计算，确保所有组成部分都被适当处理）
    q_score = sum([
        pe_vs_market if pe_vs_market is not None else 0,
        eps_growth if eps_growth is not None else 0,
        data['12Mth_Price_Momentum'][-1],
        data['1Mth_Price_Reversion'][-1],
        data['ROE'][-1] if data['ROE'][-1] is not None else 0,
        eps_growth if eps_growth is not None else 0,  # Earnings risk using eps_growth as a proxy
        eps_growth if eps_growth is not None else 0,  # Earnings momentum 3mth
        net_revisions_fy2_eps,
        fy2_eps_growth
    ])  # Simplified for demonstration; adjust weights and calculation as needed
    data['Q_Score'].append(q_score)

# 转换为DataFrame
df = pd.DataFrame(data)
df

q_score_90th_quantile = df['Q_Score'].quantile(0.9)

top_10_stocks_df = df[df['Q_Score'] >= q_score_90th_quantile]


# Creating the 'buying_list' DataFrame with specified columns
buying_list = pd.DataFrame({
    'stock_name': top_10_stocks_df['Symbol'],
    'action': ['buy'],  # Setting 'buy' as the action for all selected stocks
    'quantity': 10  # Default quantity set to 10
})

buying_list.reset_index(drop=True, inplace=True)  # Reset index for cleanliness
buying_list


# This class extends from EWrapper and EClient to handle the streaming data and send requests to Interactive Brokers
class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.nextValidOrderId = 0  

    # Override error method from EWrapper to handle errors
    def error(self, reqId, errorCode, errorString, advancedOrderRejectJson=None):
        print("Error {} {} {}".format(reqId, errorCode, errorString))
        if advancedOrderRejectJson:
            print("Advanced Order Reject Info:", advancedOrderRejectJson)

    # Override nextValidId method from EWrapper to get the next valid order ID
    def nextValidId(self, orderId):
        super().nextValidId(orderId)
        self.nextValidOrderId = orderId
        print("NextValidId:", orderId)


# Function to run the app's websocket in a separate thread
def websocket_connection():
    app.run()


# Create an instance of TradingApp and establish connection
app = TradingApp()
try:
    app.connect("127.0.0.1", 7497, clientId=1) # Set Port Number to 7497 in TWS Software for Paper Trading
    print("Connection to Interactive Broker established.")
except Exception as e:
    print("Error establishing connection:", e)

# Starting a separate daemon thread to execute the websocket connection
connection_thread = threading.Thread(target=websocket_connection, daemon=True)
connection_thread.start()
time.sleep(1)  # Adding some latency to ensure that the connection is established


# Function to create a Contract object with given parameters
def us_stock_contract(symbol, sec_type="STK", currency="USD", exchange="SMART"):
    contract = Contract()
    contract.symbol = symbol
    contract.secType = sec_type
    contract.currency = currency
    contract.exchange = exchange
    return contract

# Function to create a market order with given parameters
def marketOrder(direction, quantity):
    order = Order()
    order.action = direction
    order.orderType = "MKT"
    order.totalQuantity = quantity
    order.sweepToFill = True
    order.EtradeOnly = False
    return order

# Get the next valid order ID
order_id = app.nextValidOrderId

# Iterate over the DataFrame and place orders
for index, row in buying_list.iterrows():
    stock = row['stock_name']  # Replace 'stock_name' with your actual column name
    action = row['action']     # Replace 'action' with your actual column name
    quantity = row['quantity'] # Replace 'quantity' with your actual column name
    print(stock)
    print(action)

    # Get next valid order ID
    order_id = app.nextValidOrderId

    # Place the order
    app.placeOrder(order_id, us_stock_contract(stock), marketOrder(action, quantity))
    time.sleep(5)  # Wait for the order to process
    app.nextValidOrderId += 1
