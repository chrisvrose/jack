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

from script import mainScript

parser = argparse.ArgumentParser(description='Tose App - manager.py')
parser.add_argument('--add', action='store_true', help='Add new entry to queue')
parser.add_argument('serie', type=str, help='Serie', nargs='+')
parser.add_argument('-s', type=int, help='Season')
parser.add_argument('-e', type=int, help='Episode')

args = parser.parse_args()

serie = ' '.join(args.serie).title()
season = ""
episode = ""
mainScriptReturn = 0

if len(str(args.s)) > 2 and args.s != None:
    parser.error("Season number cannot be larger than 2")
elif args.s != None:
    season = '%02d' % args.s
if len(str(args.e)) > 2 and args.e != None:
    parser.error("Episode number cannot be larger than 2")
elif args.e != None:
    episode = '%02d' % args.e

print("[manager] args: ", " - ",serie, " - ", season, " - ", episode)

f = open("data.js", "r+")
jsondata = json.loads(f.read())
print("[manager] Current data: ",jsondata)
f.close()

if args.add:
    counter = 0
    for entry in jsondata:
        if serie in entry.values():
            counter += 1
    jsondata.append( {'serie': serie, 'season': season, 'episode': episode} )
    
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
    print("[manager] New data: \t",jsondata)

# exit()

def job():
    global mainScriptReturn
    print(time.strftime("[%H:%M:%S]", time.localtime()))
    for entry in jsondata:
        print(entry)
        
        # command = "python script.py " + entry["serie"] + " -s " + entry["season"] + " -e " + entry["episode"]
        # if entry["season"] == "":
        #     command = "python script.py " + entry["serie"] + " -e " + entry["episode"]
        # if entry["episode"] == "":
        #     command = "python script.py " + entry["serie"] + " -s " + entry["season"]
        # # print(command)
        # os.system(command)
        
        if entry["season"] and entry["episode"]:
            mainScriptReturn = mainScript(entry["serie"], entry["season"], entry["episode"])
            print("[manager][mainScript]",  mainScriptReturn)
        elif entry["season"] == "":
            mainScriptReturn = mainScript(entry["serie"], None, entry["episode"])
            print("[manager][mainScript]",  mainScriptReturn)
        elif entry["episode"] == "":
            mainScriptReturn = mainScript(entry["serie"], entry["season"], None)
            print("[manager][mainScript]",  mainScriptReturn)


## Calls job() every 15 minutes. Use every(0.1) when testing code. (Runs every 0.1 mins => 10 secs). Change back to 15 later.
schedule.every(0.1).minutes.do(job)

## Run for the first time
job()

## Actually start the loop
while True:
    checkfile = open("data.js", "r")
    print("[manager][checkfile] ", checkfile.read(), len(checkfile.read()))
    # if not len(checkfile.read()):
    print("[manager][while_loop] mainScriptReturn: ", mainScriptReturn)
    if mainScriptReturn != 0:
        print("breaking...")
        break
    schedule.run_pending()
    time.sleep(1)
    
    