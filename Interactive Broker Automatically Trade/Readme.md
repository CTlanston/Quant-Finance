### Interactive Broker Automatic Trading System

This project involves the creation of an automatic trading system using **Interactive Brokers (IB) API**. The system integrates stock market data, financial ratios, and decision-making algorithms based on **JPMorgan's Q Model** to generate trade signals and automatically execute trades. The main steps and components of this project are outlined below:

#### Key Components:

1. **Interactive Brokers (IB) API**:
   - Used to establish a connection with Interactive Brokers for both live and paper trading.
   - API enables placing buy and sell orders, retrieving market data, and managing the trading process.

2. **Data Sources**:
   - **Yahoo Finance (yfinance)**: Fetches historical market data and stock information, such as price, volume, P/E ratios, etc.
   - **Alpha Vantage API**: Retrieves additional financial metrics, such as balance sheets, market capitalization, and book-to-market ratios.

3. **Key Metrics and Calculations**:
   - **Book-to-Market Ratio**: Calculated for each stock in the list using data from Yahoo Finance and Alpha Vantage.
   - **P/E Ratio**: The price-to-earnings ratio is used for market valuation comparisons.
   - **12-Month Price Momentum and 1-Month Price Reversion**: These metrics assess stock performance over various time frames.
   - **Earnings Growth and Earnings Momentum**: Evaluate the stock’s growth in profitability, and momentum helps predict future performance.
   - **Q Score**: This score aggregates various metrics (P/E, ROE, Earnings Growth, etc.) to rank stocks.

4. **Stock Selection**:
   - The system processes a list of 30 major stocks (including companies like AAPL, MSFT, and TSLA).
   - Stocks are ranked based on the Q Score, which reflects their financial health and growth potential.
   - The top 10 stocks (based on Q Score) are selected for trading, with the system going long on these stocks.

5. **Order Execution**:
   - **Market Orders**: The system generates and places market orders through the IB API for the selected stocks.
   - For each selected stock, an order is created to buy a specified quantity of shares.
   - Each trade is automatically processed, ensuring timely execution.

6. **Multi-threaded Connection**:
   - A separate thread handles the connection to the Interactive Brokers server, ensuring smooth communication and real-time trade execution.

#### Quantitative Finance Domain Knowledge:

- **JPMorgan's Q Model**: The system's stock-ranking process mimics JPMorgan's Q Model, which involves calculating and ranking stocks based on a set of financial ratios and performance metrics. This method is widely used in quantitative finance to identify undervalued or outperforming stocks.
- **Risk Management**: By using book-to-market ratios, earnings growth, and P/E ratios, the model inherently integrates fundamental risk assessment, minimizing exposure to highly speculative stocks.
- **Automation**: Automatic trading systems, like this one, highlight the core of **algorithmic trading** in quantitative finance, which eliminates human error and improves trading efficiency.
- **Portfolio Optimization**: The system's decile-based ranking ensures that only the top-performing stocks (based on the Q Score) are included in the portfolio, similar to **long-short equity strategies** in quant finance.
