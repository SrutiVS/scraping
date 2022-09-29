
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import requests
import openpyxl
URL = "https://www.amazon.in/s?k=air+fryer"
headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0"}
page = requests.get(URL,headers=headers)
page.raise_for_status()
soup = BeautifulSoup(page.text,"html.parser")
#print(soup)
results= soup.find('div',id="search")
print(len(results))

title = results.find('h2',class_="a-size-mini a-spacing-none a-color-base s-line-clamp-2").text
rating= results.find('div', class_="a-section a-spacing-none a-spacing-top-micro").text
price = results.find('span',class_="a-price-whole").text
print (title,rating,price)

   