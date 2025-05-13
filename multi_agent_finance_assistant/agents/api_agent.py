import yfinance as yf

class APIAgent:
    def get_stock_data(self, ticker: str, period: str = "1d"):
        data = yf.download(ticker, period=period)
        return data
