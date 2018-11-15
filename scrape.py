#user hits 'acquire' to start this program
from typing import List, Any

import bs4
import re
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://www.nasdaq.com/options/'

#open connection to get the web page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

symbols = []
url = []
container = page_soup.find_all("a", {"class": "fontS16px"})

#use regex to only pull the SYMBOLS that we want
for a in container:
    symSearch = re.findall("Option Activity:(.[^<]*)", a.text)
    if symSearch:
        for r in symSearch:
            symbols.append(r.strip())
#pull the URLs that we want
for a in container:
    if re.search("Option Activity:(.[^<]*)", a.text) != None:
        print("url found")
        url.append(a.get('href'))

print("Printing symbols[]: ")
print(symbols)

print("Printing url[]: ")
print(url)
