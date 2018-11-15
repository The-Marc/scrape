# user hits 'acquire' to start this program

import bs4
import re
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://www.nasdaq.com/options/'

# open connection to get the web page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

final = []
headline = []
symbol = []
info = []
url = []
container = page_soup.find_all('a', {"class": "fontS16px"})

# use regex to only pull the SYMBOLS that we want
for a in container:
    symSearch = re.findall("Option Activity:(.[^<]*)", a.text)
    if symSearch:
        for r in symSearch:
            symbol.append(r.strip().split(", "))
# opens article page to scrape more data
for a in container:
    if re.search("Option Activity:(.[^<]*)", a.text) is not None:
        # pulls the URL
        article = a.get('href')
        url.append(article)
        # load the NEW web page of the article we want
        uClient = uReq(article)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        # pulls the headline and put into list
        headline.append(page_soup.find('h1').text)
        # pulls the text from the article
        info.append(page_soup.find('div', {"id": "articleText"}).text.strip().split('       '))

# combine the lists of lists caused by split() back into a normal list
symbolsList = []
for l in symbol:
    symbolsList += l
infoList = []
for l in info:
    infoList += l

print("Printing symbolsList[]: ")
print(symbolsList)

print("Printing url[]: ")
print(url)

print("Printing headline[]: ")
print(headline)

print("Printing infoList[]: ")
print(infoList)
