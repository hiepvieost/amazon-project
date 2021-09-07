import requests
from bs4 import BeautifulSoup
# import smtplib
import os
from twilio.rest import Client
SID = "ACf8986ccd2ab235ca7f626d1c765f037c"
TOKEN = "aae2e248219d5fd9410287a5c970e9c0"

EMAIL = "hieplecoding@gmail.com"
PASSWORD = "giahan2310"
url = "https://www.amazon.com/Apple-MWP22AM-A-cr-AirPods-Renewed/dp/B0828BJGD2/ref=sr_1_8?dchild=1&keywords=airpods&qid=1630995762&sr=8-8"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
    "Accept-Language": "en,en-US;q=0.9,de;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "html.parser")

price = soup.find(id="priceblock_ourprice").getText()

price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("$")[1]

price_as_float = float(price_without_currency)
title = soup.find(id="productTitle").get_text().strip()
if price_as_float <200:
    # message = f"{title}is now {price_as_float}"
    # with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    #     connection.starttls()
    #     result = connection.login(EMAIL, PASSWORD)
    #     connection.sendmail(
    #         from_addr=EMAIL,
    #         to_addrs=EMAIL,
    #         msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
    #     )
    client = Client(SID, TOKEN)
    message = client.messages \
        .create(
        body=f"{title}is now {price_as_float}",
        from_='+12286419463',
        to='+4367762943449'
    )
