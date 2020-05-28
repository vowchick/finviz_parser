import time
import sys
from datetime import date, timedelta
def parse_file(name):
  filea = open (name, 'r')
  d = dict()
  contents = filea.readlines()
  for x in contents:
    y = x.split()
    d[y[0]] = y[len(y) - 1]
  filea.close()
  return d

#usage : python3 3.py (today - this argument (subtract from that)) (today - this argument (subtract that))
#  chosen/first_22/4 chosen/first_22/4

def main():
  today = date.today() - timedelta (days = int (sys.argv[1]))
  yesterday = date.today() - timedelta (days=int (sys.argv[2]))
  stri = "%Y/%m/%d_"
  stri1 = "%Y/%m/%d_"
  stri += str (sys.argv[3])
  stri1 += str (sys.argv[4])
  strin = yesterday.strftime (stri)
  strin1 = today.strftime (stri1)
  strin += '.txt'
  strin1 +='.txt'
  d = parse_file (strin)
  c = parse_file (strin1)
  cnt = 0
  cnt2 = 0
  grew = []
  d_keys = d.keys()
  c_keys = c.keys()
  for x in d_keys:
    if x in c_keys:
      diff = float(c[x]) - float(d[x])
      if diff > 0:
        cnt += 1
        grew.append (x)
      else:
        cnt2 += 1
      print ('Company:', end=' ')
      print (x, end=' ')
      print ('Yesterday\'s price:', end=' ')
      print (d[x], end=' ')
      print ('Today\'s price:', end=' ')
      print (c[x], end=' ')
      print ('Price change = ', end = ' ')
      print (diff)
  print ('Grew - ', end=' ')
  print (cnt)
  print (':', grew)
  print ('Fell - ', end = ' ')
  print (cnt2)
  print (strin)
  print (strin1)



if __name__ == '__main__':
  main ()

