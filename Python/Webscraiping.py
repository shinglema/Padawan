#from urllib.request import urlopen
##url = "https://www.merriam-webster.com/dictionary/pony"
#page = urlopen(url)
#html_bytes = page.read()
#html = html_bytes.decode("utf-8")
#print(html)

import requests
from bs4 import BeautifulSoup

url = "https://www.merriam-webster.com/dictionary/pony"
html=requests.get(url).text
soup=BeautifulSoup(html)
print(soup.title)
print(soup.li)
#print(soup.find_all(class_="dtText"))
mytest=soup.find_all(class_="dtText")
print(mytest)


#//*[@id="dictionary-entry-1"]/div[2]/div[1]/span[1]/div/span[2]/span