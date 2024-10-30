from dotenv import load_dotenv
import os
import smtplib

load_dotenv()


class Posts:
    def __init__(self,id,title,subtitle,body,author,date):
        self.id = id
        self.title =title
        self.subtitle= subtitle
        self.body = body
        self.author = author
        self.date=date
class send_mail():
    def __init__(self,message,sender_mail,name,number):
        load_dotenv()
        self.email = os.getenv('EMAIL')
        self.passwo = os.getenv('APP_PASSWORD')
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=self.email, password=self.passwo)
        connection.sendmail(from_addr=self.email,
                        to_addrs=self.email,
                        msg=f"Subject:New Message\n\nName: {name}\nEmail: {sender_mail}\nPhone: {number}\nMessage:{message}")
        connection.close()