# encoding:utf-8
from pymongo import MongoClient
from bson.objectid import ObjectId
import json
import pymongo
import pprint
import sys
import datetime
from bs4 import BeautifulSoup
import requests
import locale
locale.setlocale(locale.LC_ALL, '')


client = MongoClient()
client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017/')
db = client['bot-project']
products_link = db['products']
cargo_details = db['CargoDetails']
other_details = db['OtherDetails']
price = db['Prices']

# from  config import config



i = 1


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
with requests.Session() as s:
    for data in products_link.find():
        print(data)
        productJSON = {'prod': {'url': ''},
                       'cargo_detail':
                       {'fast_delivery': '', 'free_cargo': ''},
                       'other_detail':
                       {'title': '', 'brand': '', 'seller': '',
                        'image': '', 'category': '', 'store': ''},
                       'price':
                       {'first_price': '', 'last_price': '', 'date_price': ''}}

        url2 = data['link']
        r2 = s.get(url2, headers=headers)
        if (r2.status_code == 200):
            last_key = 0
            last_key += 1
            soup2 = BeautifulSoup(r2.content, 'html5lib')
            headline2 = productJSON
            headline2['prod']['url'] = url2
            headline2['cargo_detail']['product'] = str(data['_id'])
            headline2['other_detail']['product'] = str(data['_id'])
            headline2['price']['product'] = str(data['_id'])

            if 1:
                if soup2.find("span", attrs={"class": "prc-dsc"}):
                    if soup2.find("div", attrs={"class": "add-to-basket-button-text"}):
                        headline2['other_detail']['stock'] = 1
                    else:
                        headline2['other_detail']['stock'] = 0

                    prc_slg = soup2.find(
                        "span", attrs={"class": "prc-dsc"}).text
                    if soup2.find("span", attrs={"class": "prc-org"}):
                        prc_org = soup2.find(
                            "span", attrs={"class": "prc-org"}).text
                        prc_slg = prc_slg.replace(",", ".")
                        prc_org = prc_org.replace(",", ".")
                        headline2['price']['first_price'] = prc_org
                        headline2['price']['last_price'] = prc_slg
                        headline2['price']['date_price'] = str(
                            datetime.datetime.now())
                    else:
                        prc_slg = prc_slg.replace(",", ".")
                        headline2['price']['first_price'] = prc_slg
                        headline2['price']['date_price'] = str(
                            datetime.datetime.now())

                    if 1:

                        # MARKA BURADA CEKILIYOR
                        if soup2.find("h1", attrs={"class": "pr-new-br"}):
                            myBrandElement = soup2.find(
                                "h1", attrs={"class": "pr-new-br"})
                            if myBrandElement.findNext("a"):
                                headline2['other_detail']['brand'] = myBrandElement.findNext(
                                    "a").text
                            else:
                                headline2['other_detail']['brand'] = ""

                        # TITLE BURADA CEKILIYOR
                        if soup2.find("meta", attrs={"name": "twitter:title"}):
                            headline2['other_detail']['title'] = soup2.find(
                                "meta", attrs={"name": "twitter:title"})['content']
                        else:
                            headline2['other_detail']['title']

                        # ÜRÜN RESMİ BURADA CEKILIYOR
                        if soup2.find("img", attrs={"class": "detail-section-img"}):
                            headline2['other_detail']['image'] = soup2.find(
                                "img", attrs={"class": "detail-section-img"})['src']
                        else:
                            headline2['other_detail']['image'] = ""

                        # SATICI BURADA CEKILIYOR
                        if soup2.find("a", attrs={"class": "merchant-text"}):
                            headline2['other_detail']['seller'] = soup2.find(
                                "a", attrs={"class": "merchant-text"})['href']
                        else:
                            headline2['other_detail']['seller'] = ""

                        # UCRETSIZ KARGO BURADA CEKILIYOR
                        if soup2.find("div", attrs={"class": "freeCargo"}):
                            headline2['cargo_detail']['free_cargo'] = 1
                        else:
                            headline2['cargo_detail']['free_cargo'] = 0

                        # HIZLI KARGO BURADA CEKILIYOR
                        if soup2.find("div", attrs={"class": "rushDelivery"}):
                            headline2['cargo_detail']['fast_delivery'] = 1
                        else:
                            headline2['cargo_detail']['fast_delivery'] = 0
                        # print(headline2)
                        url = 'http://localhost:3000/product/OtherDetail/add'
                        requests.post(
                            'http://localhost:3000/product/OtherDetail/add', json=(headline2['other_detail']))
                        requests.post(
                            'http://localhost:3000/product/CargoDetail/add', json=(headline2['cargo_detail']))
                        requests.post(
                            'http://localhost:3000/product/Price/add', json=(headline2['price']))
