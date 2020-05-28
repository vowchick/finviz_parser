import os
import schedule
import time
def job():
  os.system("python3 1.py")

schedule.every().day.at("22:00").do(job)
schedule.every().day.at("16:00").do(job)
while True:
  schedule.run_pending()
  time.sleep(1) # wait one minute