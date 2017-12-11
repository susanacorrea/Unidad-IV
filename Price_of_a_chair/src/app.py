__author__ = 'Alfredo y Susy'

"""Needs the modules: request, beautifulsoup4"""
from bs4 import BeautifulSoup

import requests

request = requests.get("https://www.johnlewis.com/house-by-john-lewis-hinton-office-chair/p2083183")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"itemprop": "price", "class": "now-price"})
string_price = element.text.strip() # "£129.00"
# <span itemprop="price" class="now-price"> £129.00 </span>

price_whitout_symbol = string_price[1:] # "129.00"

price = float(price_whitout_symbol)


if price < 200:
    print("You should buy the chair")
    print("The current price is {}".format(string_price))
else:
    print("You don't but, it's too expensive!")
