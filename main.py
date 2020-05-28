from chooser import *
from parser import *
from files import *
def main ():
  tickers = get_all_tickers("list.csv")
  #получили все тикеры Питерской биржы
  #получили все ссылки на компании с этими тикерами
  main_url = "https://finviz.com/quote.ashx?t="
  companies = get_all_content (tickers, main_url, 10000)

  a = get_file_name("_chosen")
  cnt = write_in_file (a, companies)
  print (cnt)
  print (len(companies))

if __name__ == '__main__':
  main ()
