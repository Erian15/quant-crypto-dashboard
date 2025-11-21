import pandas as pd
import numpy as np
from datetime import datetime
from app.data_fetch import get_multi_price_history

TICKERS = ["BTC-USD", "ETH-USD", "BNB-USD", "SOL-USD"]

def max_drawdown(series):
    cummax = series.cummax()
    dd = (series - cummax) / cummax
    return dd.min()

def main():
    today = datetime.now().strftime("%Y-%m-%d")

    # Load 1 year of data
    prices = get_multi_price_history(TICKERS, days=365)
    returns = prices.pct_change().dropna()

    report = {}

    for t in TICKERS:
        asset = prices[t]
        mdd = max_drawdown(asset.astype(float))
        daily_vol = returns[t].std()
        open_price = asset.iloc[0]
        close_price = asset.iloc[-1]

        report[t] = {
            "Open price": float(open_price),
            "Close price": float(close_price),
            "Daily volatility": float(daily_vol),
            "Max drawdown": float(mdd),
        }

    df = pd.DataFrame(report).T

    output_path = f"/home/obous/quant-crypto-dashboard/reports/daily_report_{today}.csv"

    df.to_csv(output_path)
    print(f"Report generated: {output_path}")

if __name__ == "__main__":
    main()
