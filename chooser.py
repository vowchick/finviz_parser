import csv
def get_all_tickers (csv_file_name):
    tickers = list()
    with open(csv_file_name, encoding="cp1251", newline='\n') as f:
      reader = csv.DictReader(f, delimiter=';')
      for row in reader:
        tickers.append(row['s_RTS_code'])
    return tickers
