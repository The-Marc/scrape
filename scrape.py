#user hits 'acquire' to start this program

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
print("hello")

#puts all of the elements with the titles into a container
data = []

container = page_soup.find_all("a", {"class": "fontS16px"})

#use regex to only pull the noteworthy and notable headlines
for a in container:
    search = re.search("Option Activity:", a.text)
    data.append(search)

print(data)


