import streamlit as st
import numpy as np
from data_fetch import get_price_history, get_multi_price_history


st.set_page_config(page_title="Crypto Quant Dashboard", layout="wide")

st.title("Crypto Quant Dashboard")
st.caption("A4 IF - Python, Linux & Git project")

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to:",
    ["Home", "Single Asset (Ouiam)", "Portfolio (Erian)"]
)

# ----- HOME PAGE -----
if page == "Home":
    st.subheader("Welcome ")
    st.write(
        "This dashboard is part of the *Python, Linux and Git* course. "
        "It provides single-asset and multi-asset crypto analytics."
    )

# ----- PLACEHOLDER FOR OUIAM -----
elif page == "Single Asset (Ouiam)":
    st.subheader("Single Asset Analysis – To be implemented by Ouiam")
    st.info("This page will display strategies and metrics for one asset (BTC-USD).")

# ----- YOUR PAGE: PORTFOLIO -----
elif page == "Portfolio (Erian)":
    st.subheader("Multi-Asset Crypto Portfolio")

    all_tickers = ["BTC-USD", "ETH-USD", "BNB-USD", "SOL-USD"]
    tickers = st.multiselect(
        "Select crypto assets:",
        options=all_tickers,
        default=all_tickers
    )

    days = st.slider(
        "Time window (days):",
        min_value=30,
        max_value=365,
        value=180,
        step=10
    )

    if len(tickers) == 0:
        st.warning("Please select at least one asset.")
    else:
        # 1) Load prices
        prices = get_multi_price_history(tickers, days=days)

        st.subheader("Daily close prices")
        st.line_chart(prices)

        # 2) Compute daily returns
        returns = prices.pct_change().dropna()

        # 3) Equal-weight portfolio (for now)
        n_assets = len(tickers)
        weights = np.ones(n_assets) / n_assets  # vector of 1/n

        # portfolio return each day = sum(weights * asset_returns)
        portfolio_returns = (returns * weights).sum(axis=1)

        # 4) Portfolio value starting at 1.0
        portfolio_value = (1 + portfolio_returns).cumprod()

        st.subheader("Portfolio value (base = 1.0)")
        st.line_chart(portfolio_value)

        st.subheader("Basic statistics")
        col1, col2 = st.columns(2)

        with col1:
            st.write("Average daily return:", float(portfolio_returns.mean()))
            st.write("Daily volatility:", float(portfolio_returns.std()))

        with col2:
            st.write("Number of assets:", n_assets)
            st.write("Time window (days):", days)
