import pandas as pd
from bs4 import BeautifulSoup
import csv
import requests
import json
from html.parser import HTMLParser
URL ="https://www.bigbasket.com/custompage/sysgenpd/?type=pc&slug=lips"
headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0"}
page=requests.get(URL,headers=headers)
#page.raise_for_status()
page_dict =page.json() #creating python dictionary
#print(page_dict)
pretty=json.dumps(page_dict,indent=4) #pretty printing json object
#print(pretty)
soup = BeautifulSoup(page.content,"html.parser")
#print(soup.prettify())
#print(len(pd_list))
#df=pd.DataFrame(page_dict.get('related_search'))
#print(df)
comp=json.loads(page.text)
#print(comp)
comp =comp['tab_info']
#comp[0]
a = []
for i in comp[0]['product_info']['products']:
   a.append(i)
print(a)
pd_name = []
pd_mrp = []
pd_brand = []
pd_sprice=[]
pd_rating=[]
for j in a:
    pd_name.append(j['p_desc'])
    pd_mrp.append(j['mrp'])
    pd_brand.append(j['p_brand'])
    pd_sprice.append(j['sp'])
    pd_rating.append(j['rating_info'].get('avg_rating'))
#print(name)
#print(mrp)
#print(rating)
    
    
pd_details=pd.DataFrame({'Product_name':pd_name,'Product_Brand':pd_brand,'MRP':pd_mrp,'Special_price':pd_sprice,'Product_Rating':pd_rating})
pd_details.to_csv("Bigbasket.csv")