from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError

def getTitle(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        print(e)
    if html is None:
        print("URL is not found")
    else:
        try:
            bsObj= BeautifulSoup(html.read(), 'lxml')
            nameList=bsObj.findAll("span", {"class":"green"})
            for name in nameList:
                print(name.get_text())
        except AttributeError as e:
            return None
    
title= getTitle("http://www.pythonscraping.com/pages/warandpeace.html")
