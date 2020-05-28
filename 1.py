import requests
from bs4 import BeautifulSoup
from abcdmy import *
from threading import Thread
import time
import datetime
import os

def main ():
  url = 'https://finviz.com/screener.ashx'
  url2 = "?v=111&f=fa_debteq_u0.5,fa_epsyoy_pos,fa_pb_u3,fa_pc_low,fa_pe_low,fa_pfcf_low,fa_ps_u3&ft=2&r="
  url3 = "?v=111&r="
  ds2 = get_all_the_contents (6, url, url3)
  ds = get_all_the_contents (6, url, url2)
  today = datetime.datetime.today()
  print ('allright!')
  create_dir (today)
  strin = "%Y/%m/%d_chosen_"
  strin2 = "%Y/%m/%d_first_"
  if datetime.datetime.today().hour != 22:
    strin += "4"
    strin2 += "4"
  else:
    strin += "22"
    strin2 += "22"
  
  print (datetime.datetime.today().hour)
  a = today.strftime(strin)
  a = a + '.txt'
  b = today.strftime(strin2)
  b = b + '.txt'
  write_in_file (a, ds)
  write_in_file (b, ds2)




if __name__ == '__main__':
  main ()