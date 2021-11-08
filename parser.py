from ast import parse
import sys
import fetcher
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def print_stuff (company):
  print (company['title'], end=' ')
  print ('EPS', company['EPS this Y'], end=' ')
  print ('P/B', company['P/B'], end=' ')
  print ('P/E', company['P/E'], end=' ')
  print ('Sales Q/Q', company['Sales Q/Q'])

def get_all_apropriate_tickers (tickers, main_url, num, print_all):
  cnt = 0
  comps = dict ()
  for ticker in tickers:
    cnt += 1
    if cnt > num:
      break
    try:
      link_to_ticker = main_url + ticker + "&ty=c&p=d&b=1"
      html_of_the_page = fetcher.get_html(link_to_ticker)
      d = parse_one_company(html_of_the_page)
      d['title'] = ticker
      company = d
      if len (company) > 0:
        # print ('pe', company['P/E'])
        # print ('sales', company['Sales Q/Q'][:-1])
        # print ('eps', company ['EPS this Y'][:-1])
        # print ('pb', company['P/B'])
        # print ('ps', company['P/S'])
        if "P/S" and "P/E" and "P/B" and "Price"  and "Sales Q/Q" in company:
          if (float (company['P/E']) < 35                               and
              float (company['Sales Q/Q'][:-1]) > 0                     and
              float (company ['EPS this Y'][:-1]) > 0                   and
              float (company['P/B']) < 3                                and
              float (company['P/S']) < 4                                #and
           #   company['Sales Q/Q']  > company['Sales past5Y']
          ):
            comps[ticker] = company
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
    except Exception as e: sys.stderr.write(str (e) + "\n")
  return pd.DataFrame.from_dict (comps).transpose ()

def get_ticker (link):
  start = link.index ('=')
  end = link.index ('&')
  return link[start + 1 : end]

def parse_all_companies (links):
  companies = dict ()
  for link in links:
    company = parse_one_company (fetcher.get_html (link))
    ticker = get_ticker (link)
    companies[ticker] = company
  return pd.DataFrame.from_dict (companies)

def crop_table (table):
    drop_indeces = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54, 56, 57, 58, 59, 60, 61,62,63,65,66,67,68,69,70]
    return table.drop (drop_indeces)

def map_to_float (x):
    if (x == '-'):
        return 0.0
    elif '%' in x:
        return float (x[:-1])
    else:
        try:
            return float (x)
        except:
            return x

def crop_companies (companies):
  companies = crop_table (companies)
  companies.applymap (map_to_float)

def parse_one_company(html):

    soup = fetcher.get_soup (html)
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