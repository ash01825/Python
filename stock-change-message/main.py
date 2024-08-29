import os
import requests
import datetime
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(r"/Users/ash/Desktop/Python/stock-change-message/.env")

STOCK = os.getenv("STOCK")
COMPANY_NAME = os.getenv("COMPANY_NAME")
API_KEY_STOCK = os.getenv("API_KEY_STOCK")
API_KEY_NEWS = os.getenv("API_KEY_NEWS")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
VERIFIED_PHONE_NUMBER = os.getenv("VERIFIED_PHONE_NUMBER")

today = datetime.datetime.today()

if today.weekday() < 5:
    url_stocks = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}.BSE&outputsize=compact&apikey={API_KEY_STOCK}"
    r = requests.get(url=url_stocks)
    data_stocks = r.json()
    
    if "Time Series (Daily)" in data_stocks:
        time_series = data_stocks["Time Series (Daily)"]

        keys = list(time_series.keys())

        today_close = float(time_series[keys[0]]["4. close"])
        yesterday_close = float(time_series[keys[1]]["4. close"])

        percent_change = ((today_close - yesterday_close) / yesterday_close) * 100
        if abs(percent_change) > 5:
            url_news = f"https://newsapi.org/v2/top-headlines?country=in&category=business&q={COMPANY_NAME}&apiKey={API_KEY_NEWS}"
            d = requests.get(url=url_news)
            data_news = d.json()
            top_3_articles = data_news.get('articles', [])[:3]

            message_to_send = [
                f"Headline: {article['title']}. \nBrief: {article['description']}"
                for article in top_3_articles
            ]

            client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
            for m in message_to_send:
                message = client.messages.create(
                    from_=TWILIO_PHONE_NUMBER,
                    body=m,
                    to=VERIFIED_PHONE_NUMBER
                )
    else:
        print("Time Series data not found in stock response.")
        print("API Response:", data_stocks)
