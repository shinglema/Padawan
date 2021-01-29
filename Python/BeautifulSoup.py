import requests
import webbrowser
import re
from bs4 import BeautifulSoup
from pprint import pprint

webbrowser.open("https://www.merriam-webster.com/dictionary/pony")

resp=requests.get("https://www.merriam-webster.com/dictionary/pony")

html=resp.text

soup=BeautifulSoup(html,"lxml")
#print(soup.prettify())
#print(soup.img)
print(soup.strong)

rows = soup.find_all('span')


cells = soup.find_all('strong')

for cell in cells:
    print(cell.text)



#for tr in soup.find_all('tr'):
 #   for td in tr.find_all('td'):
  #      print(td.text.strip())
