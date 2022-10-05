
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import requests
for i in range (1,30):

    URL = "https://www.amazon.in/s?k=air+fryer&page=i"
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0"}
    output_file = open("Air-Fryer-Amazon.txt","w")
    #extracting html source code of this page
    page = requests.get(URL,headers=headers)
    #checking whether the url has any issues
    page.raise_for_status()
    #parsing the html text using html.parser
    soup = BeautifulSoup(page.text,"html.parser")
    #print(soup)
    #finding all the search items
    results= soup.find_all('div',{'data-component-type':'s-search-result'})
    print(len(results))
# printing the details of the page

    for result in results:
        atag=result.h2.a
        title = atag.text.strip()

        price = result.find('span',{'class':'a-offscreen'}).text

        rating = result.i.text

        print(title,price,rating)
        #writing details to a file

        output_file.write(title+"\n "+price+"\n"+rating+"\n"+"\n\n")
        

   