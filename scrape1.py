from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError

def getTitle(url):
    try:
        html=urlopen(url)
    
        if html is None:
            print("URL is not found")
        else:
            try:
                bsObj= BeautifulSoup(html.read(), 'lxml')
                title=bsObj.body.h1
            except AttributeError as e:
                return None
        return title
    except HTTPError as e:
        print(e)
    
title= getTitle("https://www.mustakbil.com")
if(title==None):
    print("Title could not be found")
else:
    print(title)
