import requests
from bs4 import BeautifulSoup
def get_all_links (main_url, tickers):
    links = list()
    for ticker in tickers:
      link_to_ticker = main_url + ticker + "&ty=c&p=d&b=1"
      links.append(link_to_ticker)
    return links
def get_all_content(tickers, main_url, num):
  all = list ()
  cnt = 0
  for ticker in tickers:
    cnt += 1
    if cnt > num:
        break
    try:
      link_to_ticker = main_url + ticker + "&ty=c&p=d&b=1"
      d = parse_one_company(get_html(link_to_ticker))
      d['title'] = ticker
      all.append(d)
    except:
      print("Couldn't do something with", ticker)
  return all
def get_html (url):
  headers = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0'}
  r = requests.get(url, headers=headers)
  return r.text         ## возвращает html - код страницы

def parse_one_company(html):
    soup = BeautifulSoup (html, 'lxml')
    text = []
    values = []

    try:
      valss = soup.find ('table', class_="snapshot-table2")
      vals = valss.find_all('td', class_="snapshot-td2")
      for val in vals:
        a = val.text
        values.append (a)
      tds = soup.find ('table', class_="snapshot-table2").find_all('td', class_="snapshot-td2-cp")
      for td in tds:
        a = td.text
        text.append (a)
      d =  dict()
      length = len(tds)
      for i in range (length):
        d[text[i]] = values[i]
      return d
    except:
        return dict()
