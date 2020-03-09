import datetime
import schedule
import time
from dirsync import sync

def job():
  print(datetime.datetime.now())
  sync("./a", "./b", "sync", "-p")

schedule.every(0.1).minutes.do(job)

while True:
  schedule.run_pending()
  time.sleep(1)
