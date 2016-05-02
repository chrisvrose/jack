## manager.py
## This is the main script to run as it runs script.py periodically.
## For syntax of calling script.py, check first few commented into lines of script.py


import schedule
import time
import os

def job():
    print time.strftime("[%H:%M:%S]", time.gmtime())
    os.system("python script.py 'quantico' -s 1 -e 20")


## Calls job() every 15 minutes.
schedule.every(15).minutes.do(job)

## Run for the first time
job()

## Actually start the loop
while True:
    schedule.run_pending()
    time.sleep(1)