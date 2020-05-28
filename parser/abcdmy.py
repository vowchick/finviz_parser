import requests
from bs4 import BeautifulSoup
import os
import datetime
def get_html (url):
  r = requests.get (url)
  return r.text         ## возвращает html - код страницы

def get_all_links (html):
  soup = BeautifulSoup (html, 'lxml')
  tds = set()
  tds = soup.find_all('a', class_='screener-link-primary') # ищет все штуки вида <a href="..." class="screener-link-primary">
  links = set ()
  link = 'https://finviz.com/'
  for td in tds:
    a = td.get('href') # собственно получает ссылку
    links.add (link + a)
  return links


def write_in_file (a, ds):
  file = open (a, 'w+')
  for d in ds:
      file.write (d['ticker'])
      file.write (' ')
      file.write (d['title'])
      file.write (' ')
      file.write (d['Price'])
      file.write ('\n')
  file.close ()

def get_all_the_contents(num, url, url2):
  a = -21
  d = []
  b = url2
  for i in range (num):
    a = a + 20
    all_links = get_all_links (get_html (url + b + str (a)))
    for i in all_links:
      d.append (parse_int_link (get_html (i)))
  return d

def parse_int_link (html):
  soup = BeautifulSoup (html, 'lxml')
  title = soup.find ('title')
  text = []
  valls = []
  vals = soup.find ('table', class_="snapshot-table2").find_all('td', class_="snapshot-td2")
  for val in vals:
    a = val.text
    valls.append (a)
  tds = soup.find ('table', class_="snapshot-table2").find_all('td', class_="snapshot-td2-cp")
  for td in tds:
    a = td.text
    text.append (a)
  d =  dict()
  length =  len(tds)
  for i in range (length):
    d[text[i]] = valls[i]
  txt = title.get_text ()
  txt = txt.split (' ')
  d['ticker'] = txt[0];
  txt.remove (txt[0])
  texxt = ''
  for tx in txt:
    texxt = texxt + tx + ' '
  d['title'] = texxt
  return d


def create_dir (today):
  a = today.strftime("%Y/%m")
  if not os.path.exists(a):
    os.makedirs(a)

#url = 'https://finviz.com/quote.ashx?t=A&ty=c&p=d&b=1'

#r = requests.get (url)

#soup = BeautifulSoup (r.text, 'lxml')
#with open('a.txt', 'w') as file:
 # file.write (soup.prettify())