import schedule
import time
import os

def job():
    print time.strftime("[%H:%M:%S]", time.gmtime())
    os.system("python script.py 'quantico' -s 1 -e 20")

schedule.every(15).minutes.do(job)
job()
while True:
    schedule.run_pending()
    time.sleep(1)