#still gotta run this in a cloud with AWS Lambda or maybe Google Cloud FUnctions

import datetime as dt
import random
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

email = os.getenv('EMAIL')
passwo = os.getenv('APP_PASSWORD')

now = dt.datetime.now()
day=now.weekday()
if day==0:
    with open("working-with-email\quotes.txt") as file:
        quotes=file.readlines()
        message=random.choice(quotes)

    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=email, password=passwo)
    connection.sendmail(from_addr=email,
                        to_addrs="deadasf42@gmail.com",
                        msg=f"Subject: Bot mail\n\n{message}")
    connection.close()

    print(message)    

