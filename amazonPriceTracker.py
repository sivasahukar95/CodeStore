import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.in/Test-Exclusive-748/dp/B07DJLVJ5M/ref=sr_1_1?dchild=1&keywords=oneplus+7t&qid=1595435742&sr=8-1"
HEADERS ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
Required_price = 35000.00
EMAIL_ADDRESS= "sivasahukar95@outlook.com"


def compare():
    price = eval(TitlePrice())
    if price>=Required_price:
        diff= price - Required_price
        print("the required price is still {}".format(diff))
    else:
        print("the price of the product is cheaper now ... Hurry up !!!")
        sendmail()


def TitlePrice():
    page= requests.get(URL, headers=HEADERS)
    soup= BeautifulSoup(page.content, "html.parser")
    title = soup.find(id = "productTitle").get_text().strip()
    price= soup.find(id= "priceblock_dealprice").get_text().strip()[1:8]
    price=price[1:]
    price_ar= price.split(",")
    price=''.join(price_ar)
    print()
    print(title)
    print(price)
    return price

def sendmail():
    subject= "Hey there bud !! the price has been dropped hurry Up !!!!"
    body = "subject:" + subject+'\n\n'+URL
    server = smtplib.SMTP(host='smtp.outlook.com', port = 587)
    server.ehlo()
    server.starttls()
    server.login(EMAIL_ADDRESS, 'bobMarley')
    server.sendmail(EMAIL_ADDRESS,EMAIL_ADDRESS, body)
    print("mail sent sucessfully")
    pass 

if __name__=="__main__":
    while True:
        compare()
        time.sleep(40)