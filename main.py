from chooser import *
from parser import *
import sys
def main ():
  tickers = get_all_tickers("list.csv")
  #получили все тикеры Питерской биржы
  #получили все ссылки на компании с этими тикерами
  main_url = "https://finviz.com/quote.ashx?t="
  companies = get_all_apropriate_tickers(tickers, main_url, int (sys.argv[1]), int (sys.argv[2]))

if __name__ == '__main__':
  main ()
