import os
import time
import datetime
def create_dir (today):
  a = today.strftime("%Y/%m")
  if not os.path.exists(a):
    os.makedirs(a)
def write_in_file (file_name, companies):
    file = open(file_name, "w")
    cnt = 0
    for company in companies:
      if len (company) > 0:
        if "P/E" and "P/B" and "Price" and "Dividend" in company:
          if (company['P/E'] < '20' and
          company['P/B'] < '2' and
          company['Price'] < '300' and
          company['Dividend'] != '-' and
          company['P/E'] != '-'
          ):
            file.write (company['title'])
            file.write (" P/E =  ")
            file.write (company['P/E'])
            file.write (" P/B =  ")
            file.write(company['P/B'])
            file.write (" Price = ")
            file.write (company['Price'])
            file.write ("\n")
            cnt += 1
    print (cnt)
    file.close()
    return cnt
def get_file_name (plus):
    today = datetime.datetime.today()
    create_dir (today)
    strin = "%Y/%m/%d"
    a = today.strftime(strin)
    a = a + plus
    a = a + '.txt'
    return a
