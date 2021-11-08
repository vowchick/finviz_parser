from parser import * 
from chooser import *
from fetcher import *
import pandas as pd
import sys

table_name = "after.csv"
def main ():
  tickers = get_all_tickers("list.csv")
  #получили все тикеры Питерской биржы
  main_url = "https://finviz.com/quote.ashx?t="
  # link = "https://finviz.com/screener.ashx?v=111&"
  # links = get_all_links (link, 5000) 
  # print ("got all links")
  # companies = parse_all_companies (links)
  # print ("Parsed all links")
  # companies.to_csv (table_name)
  # print ("Converted to csv")
  # companies = pd.read_csv (table_name)
  # print ("Got back brom csv")
  # companies = crop_table (companies)
  # print ("Croped")
  # companies.to_csv (table_name)  
  # print ("Done")

  companies = get_all_apropriate_tickers(tickers, main_url, int (sys.argv[1]), int (sys.argv[2]))
  companies.to_csv ("tickers_november.csv")

if __name__ == '__main__':
  main ()
