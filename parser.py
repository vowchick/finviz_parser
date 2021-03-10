import requests
from bs4 import BeautifulSoup
def get_all_links (main_url, tickers):
    links = list()
    for ticker in tickers:
      link_to_ticker = main_url + ticker + "&ty=c&p=d&b=1"
      links.append(link_to_ticker)
    return links
def print_stuff (company):
  print (company['title'], end=' ')
  print ('EPS', company['EPS this Y'], end=' ')
  print ('P/B', company['P/B'], end=' ')
  print ('P/E', company['P/E'], end=' ')
  print ('Sales Q/Q', company['Sales Q/Q'])

def get_all_apropriate_tickers (tickers, main_url, num, print_all):
  cnt = 0
  for ticker in tickers:
    cnt += 1
    if cnt > num:
      break
    try:
      link_to_ticker = main_url + ticker + "&ty=c&p=d&b=1"
      html_of_the_page = get_html(link_to_ticker)
      d = parse_one_company(html_of_the_page)
      d['title'] = ticker
      company = d
      if len (company) > 0:
        if "P/S" and "P/E" and "P/B" and "Price" and "Dividend" and "Sales Q/Q" in company:
          if (company['P/E'] < '25'       and
          company['Sales Q/Q'] > '0.0%'   and
          company ['EPS this Y'] > '0.0%' and
          company['P/B'] < '3'            and
          company['P/S'] < '4'            and
          company['Price'] < '500'        and
          company['Dividend'] != '-'      and
          company['P/E'] != '-'
          ):
            if print_all == 1:
              print_stuff (company)
            else:
              print (company['title'])
            # file.write (" P/E =  ")
            # file.write (company['P/E'])
            # file.write (" P/B =  ")
            # file.write(company['P/B'])
            # file.write (" Price = ")
            # file.write (company['Price'])
            # file.write ("\n")
    except:
      print("Couldn't do something with", ticker)

def get_html (url):
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Max OS X 10.16; rv:86.0) Gecko/20100101 Firefox/86.0'}
  
  r = requests.get(url, headers=headers)
  ##print (r.text)
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
      x = 1
    return dict()
