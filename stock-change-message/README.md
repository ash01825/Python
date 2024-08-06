# Stock Change Message

This Python project is designed to send notifications about stock price changes. It monitors specific stocks and alerts users when the price of a stock changes by a certain percentage.

## Features

- Monitors stock prices in real-time.
- Sends notifications when the price changes by a specified percentage.
- Customizable stock list and change thresholds.

## Requirements

- Python 3.x
- [Install additional dependencies if any are used, e.g., requests, smtplib]

## Installation

1. Clone the repository:

    bash
    git clone https://github.com/ash01825/Python.git
    cd Python/stock-change-message
    

2. Install the required packages:

    bash
    pip install -r requirements.txt
    

3. Configure your stock list and alert thresholds in config.py (or wherever your configuration is set).

## Usage

Run the script to start monitoring stock prices:

```bash
python monitor_stocks.py
