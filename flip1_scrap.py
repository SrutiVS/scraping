import pandas as pd
from bs4 import BeautifulSoup
import csv
import requests
from html.parser import HTMLParser
page_num= input ("Enter number of page numbers:")
for r in range(1,int(page_num)):
    URL= "https://www.flipkart.com/search?q=air+fryer&sid=j9e%2Cm38%2Cj1e&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=air+fryer%7CAir+Fryers&requestId=dadfe4e4-56a6-4849-8691-9eeb601df480&page="+str(r)
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0"}
    page = requests.get(URL,headers=headers)
    page.raise_for_status()
    soup = BeautifulSoup(page.text,"html.parser")
    #print(soup)
    products=[]
    prices=[]
    ratings=[]
    flip_results = soup.find_all('div',{'class':'_4ddWXP'})
    print (len(flip_results))
    for i in flip_results:
        pd_name = i.find('a',{'class':'s1Q9rs'}).text
        print(pd_name)
        price = i.find('div',{'class':'_30jeq3'}).text
        print(price)
        rating = i.span.text
        print(rating)
        products.append(pd_name)
        ratings.append(rating)
        prices.append(price)
    df = pd.DataFrame({'Product Name':products,'Prices':prices,'Ratings':ratings})
    df.head()
    df.to_csv('air_fryer.csv')


