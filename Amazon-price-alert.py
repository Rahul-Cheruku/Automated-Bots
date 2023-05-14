import requests
from bs4 import BeautifulSoup
from smtplib import SMTP
import lxml

FROM_ADD = 'example_from@gmail.com'
TO_ADD = 'example_to@gmail.com'
PASSWORD = 'psd'
def send_alert(product_name, listed_price):
    with SMTP('smtp.gmail.com', port=587) as connection:
        MESSAGE=f"Subject: AMAZON LOW PRICE ALERT\n\n{product_name} is listed at {listed_price}, hurry up!"
        connection.starttls()
        connection.login(user=FROM_ADD,password=PASSWORD)
        connection.sendmail(from_addr=FROM_ADD, to_addrs=TO_ADD, msg=MESSAGE.encode('utf-8'))
    print("message Sent")



HEADER = {
    "Request Line": "GET / HTTP/1.1",
    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    # "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    # "Connection": "keep-alive",
    # "Host": "myhttpheader.com",
    # "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}
URL = "https://www.amazon.in/Redmi-9A-Sport-Octa-core-Processor/dp/B09GFLXVH9/ref=lp_1389401031_1_5"
DESIRED_PRICE = 7500
response = requests.get(url=URL, headers=HEADER)
print(response.text)
soup = BeautifulSoup(response.text, "lxml")

name = soup.find("span", id="productTitle").getText().strip()

price = soup.find(name="span", class_="a-offscreen").getText()
amount = float(price.split('₹')[1].replace(",", ""))

if DESIRED_PRICE >= amount > 1:
    send_alert(product_name=name, listed_price=price)
    print("Sending alert.......")
print(name)
print(price)


