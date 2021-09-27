from chooser import *
from fetcher import *
import sys

def main ():
  tickers = get_all_tickers("list.csv")
  #получили все тикеры Питерской биржы
  main_url = "https://finviz.com/quote.ashx?t="
  link = "https://finviz.com/screener.ashx?v=111&"
  tickers = get_all_links (link, 10)
  print (tickers)
  #companies = get_all_apropriate_tickers(tickers, main_url, int (sys.argv[1]), int (sys.argv[2]))

if __name__ == '__main__':
  main ()
