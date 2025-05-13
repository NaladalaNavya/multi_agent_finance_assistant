import yfinance as yf
import pandas as pd

class APILoader:
    def fetch_historical_data(self, ticker: str, period: str = "1mo") -> pd.DataFrame:
        data = yf.download(ticker, period=period)
        return data

    def fetch_realtime_price(self, ticker: str) -> float:
        stock = yf.Ticker(ticker)
        return stock.info.get("currentPrice", 0.0)
