import pandas as pd
from datetime import datetime, timedelta
import yfinance as yf


def get_price_history(ticker: str, days: int = 90) -> pd.DataFrame:
    """
    Download historical daily prices for a single asset.
    Returns a DataFrame with a 'price' column indexed by date.
    """
    end = datetime.today()
    start = end - timedelta(days=days)

    data = yf.download(ticker, start=start, end=end)

    df = data[["Close"]].rename(columns={"Close": "price"})
    df.index.name = "date"
    return df


def get_multi_price_history(tickers, days: int = 90) -> pd.DataFrame:
    """
    Download historical daily close prices for several assets.
    Returns a DataFrame where columns are tickers and rows are dates.
    """
    end = datetime.today()
    start = end - timedelta(days=days)

    data = yf.download(tickers, start=start, end=end)["Close"]
    data.index.name = "date"
    return data
