# Crypto Quant Dashboard

Students:

- Erian STANLEY YOGARAJ
- Ouiam BOUSSAID BENCHAARA

Program: ESILV – A4 IF1

Project Overview

The Crypto Quant Dashboard is a quantitative cryptocurrency analysis project developed using Python, Streamlit, Git, and Linux.

The goal of this project is to reproduce a realistic quantitative finance workflow: market data is automatically retrieved, analyzed, visualized, and deployed on a Linux environment.

The dashboard is composed of two complementary modules developed collaboratively:

- Quant A – Single Asset Analysis (Ouiam)
- Quant B – Multi-Asset Portfolio Analysis (Erian)

Both modules are fully integrated into a single interactive Streamlit application.

1. Project Objectives

- Retrieve cryptocurrency market data with automatic refresh.
- Build an interactive and professional dashboard using Streamlit.
- Implement single-asset trading strategies and performance analysis.
- Design a multi-asset portfolio with advanced quantitative metrics.
- Compute key financial indicators: returns, volatility, Sharpe ratio, correlation, maximum drawdown.
- Generate an automated daily financial report using Linux cron.
- Apply a clean Git collaboration workflow.
- Deploy the application on Linux with continuous (24/7) execution.

2. Features

Quant A – Single Asset Analysis (Ouiam)

- Assets analyzed: BTC-USD, ETH-USD
- Daily close price visualization
- Performance metrics on daily and annualized bases
- Trading strategies:
  - Buy & Hold
  - SMA Crossover
  - RSI Strategy
- Bonus: 14-day price prediction using linear regression
- Metrics: average return, volatility, Sharpe ratio, max drawdown

Quant B – Multi-Asset Portfolio Analysis (Erian)

- Assets: BTC-USD, ETH-USD, BNB-USD, SOL-USD
- Multi-asset visualization
- Portfolio construction with manual and risk-based weights
- Portfolio metrics and correlation analysis
- Portfolio vs BTC comparison

3. Project Structure

quant-crypto-dashboard/
├── app/
│ ├── main.py
│ ├── data_fetch.py
├── reports/
├── report.py
├── run.sh
├── requirements.txt
└── README.md

4. Installation

git clone https://github.com/Erian15/quant-crypto-dashboard.git
cd quant-crypto-dashboard
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

5. Running the Dashboard

streamlit run app/main.py

Background execution:
chmod +x run.sh
./run.sh

6. Daily Automated Report

A daily CSV report is generated automatically at 20:00 using cron.
Reports are saved in the reports/ directory.

7. Conclusion

This project demonstrates a complete quantitative finance pipeline combining Python, data analysis, visualization, Git collaboration, and Linux automation.
