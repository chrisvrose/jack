#!python3
## manager.py
## This is the main script to run as it runs script.py periodically.
## For syntax of calling script.py, check first few commented into lines of script.py

import schedule
import time
import os
import argparse
import urllib.request, urllib.parse, urllib.error
import json


parser = argparse.ArgumentParser(description='Tose App - manager.py')
parser.add_argument('action', type=str, help='Action')
parser.add_argument('serie', type=str, help='Serie')
parser.add_argument('-s', type=int, help='Season')
parser.add_argument('-e', type=int, help='Episode')

args = parser.parse_args()

serie = args.serie
season = ""
episode = ""
if  args.serie == "":
    parser.error("Invalid serie")
if len(str(args.s)) > 2 and args.e != None:
    parser.error("Season number cannot be larger than 2")
elif args.s != None:
    season = '%02d' % args.s
if len(str(args.e)) > 2 and args.e != None:
    parser.error("Episode number cannot be larger than 2")
elif args.e != None:
    episode = '%02d' % args.e


if args.action.lower() == 'add':
    counter = 0
    f = open("data.js", "r+")
    jsondata = json.loads(f.read())
    print(jsondata)
    for entry in jsondata:
        if serie in entry.values():
            counter += 1
    print(counter)
    jsondata.append( {'serie': serie, 'season': season, 'episode': episode} )
    f.close()
    
    if not counter:
        print("Writing to file")
        f = open("data.js", "w+")
        f.write(json.dumps(jsondata))
        f.close()
    else:
        print("Already exists, Replacing")
        for i in range(len(jsondata)):
            if jsondata[i]["serie"] == serie:
                jsondata.pop(i)
                break
        f = open("data.js", "w+")
        f.write(json.dumps(jsondata))
        f.close()


def job():
    print(time.strftime("[%H:%M:%S]", time.gmtime()))
    for entry in jsondata:
        print(entry)
        
        command = "python script.py '" + entry["serie"] + "' -s " + entry["season"] + " -e " + entry["episode"]
        if entry["season"] == "":
            command = "python script.py '" + entry["serie"] + "' -e " + entry["episode"]
        if entry["episode"] == "":
            command = "python script.py '" + entry["serie"] + "' -s " + entry["season"]
        # print(command)
        os.system(command)


## Calls job() every 15 minutes. Use every(0.1) when testing code. (Runs every 0.1 mins => 10 secs). Change back to 15 later.
schedule.every(15).minutes.do(job)

## Run for the first time
job()

## Actually start the loop
while True:
    schedule.run_pending()
    time.sleep(1)
    checkfile = open("data.js", "r")
    if not len(checkfile.read()):
        break