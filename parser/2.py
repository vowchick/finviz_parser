import requests
from bs4 import BeautifulSoup

url = 'https://finviz.com/quote.ashx?t=AACG&ty=c&p=d&b=1'

r = requests.get (url)

soup = BeautifulSoup (r.text, 'lxml')
with open('a.txt', 'w') as file:
  file.write (soup.prettify())