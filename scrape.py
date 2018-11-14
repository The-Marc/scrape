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

data = []
container = page_soup.find_all("a", {"class": "fontS16px"})

#use regex to only pull the noteworthy and notable symbols from the headlines
for a in container:
    symSearch = re.findall("Option Activity:(.[^<]*)", a.text)
    if symSearch:
	    for r in symSearch:
                data.append(r.strip())
                print(r)

print("Printing data[]: ")
print(data)
