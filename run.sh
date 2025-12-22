#!/bin/bash

# Absolute project path
PROJECT_DIR="/home/obous/quant-crypto-dashboard"

# Activate virtual environment
source $PROJECT_DIR/.venv/bin/activate

# Run Streamlit in background
nohup $PROJECT_DIR/.venv/bin/streamlit run $PROJECT_DIR/app/main.py \
    --server.address=0.0.0.0 \
    --server.port=8501 \
    > $PROJECT_DIR/streamlit.log 2>&1 &

echo " Crypto Quant Dashboard is running in background on port 8501"
