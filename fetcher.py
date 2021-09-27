from main import main
import requests
import sys
from bs4 import BeautifulSoup

link_start = "https://finviz.com/"

def get_all_links_only_spb (main_url, tickers):
    links = list()
    for ticker in tickers:
      link_to_ticker = main_url + ticker + "&ty=c&p=d&b=1"
      links.append(link_to_ticker)
    return links


def get_all_links (main_url, cnt):
  all_links = set ()
  for i in range (cnt):
    page_link = main_url + "r=" + str (20 * i + 1)
    all_links.update (get_all_links_at_page (get_html (page_link)))

  return all_links

def get_soup (html):
  try:
    soup = BeautifulSoup (html, 'lxml')
  except:
    print ("Couldn't parse")
    soup = set ()
  return soup

def get_all_links_at_page (html):
  
  soup = get_soup (html)
  soup_set = soup.find_all ('a', class_="screener-link")

  links = set (link_start + x.get ('href') for x in soup_set)
  return links
  
def get_html (url):
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Max OS X 10.16; rv:86.0) Gecko/20100101 Firefox/86.0'}
  r = requests.get(url, headers=headers)
  #print (r.text)
  return r.text         ## возвращает html - код страницы
