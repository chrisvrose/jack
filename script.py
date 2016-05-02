#!python3
## script.py
## This script does most of the work. Heavily commented.
## Run this manually by:
## python script.py <serie> -s <season no.> -e <episode no.>
## -s and -e are optional. Read lines 57-68. Use whenever possible for best results.
## eg.: python script.py The Flash -s 2 -e 14

import feedparser
import urllib.parse
import argparse
import os, json


#### Get arguments passed ####
parser = argparse.ArgumentParser(description='Tose App - More description goes here.')
# Serie
parser.add_argument('serie', type=str, help='Serie', nargs='*')
# Season
parser.add_argument('-s', type=int, help='Season')
# Episode
parser.add_argument('-e', type=int, help='Episode')


# All variables stored in 'args' array
args = parser.parse_args()


#### Making sure that the serie, season and episode are not invalid ####
serie = urllib.parse.quote(' '.join(args.serie), safe='')
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


#### Printing just for fun ####
print("Argument values:")
print(("Serie: " + serie + "\t" + "Season: " + season + "\t" + "Episode: " + episode))


#### Init some variables that are required. ####
counter = 0                     # Stores the number of optimal results
resultSizes = []                # Stores all sizes of optimal results
resultTitles = []               # Stores all titles of optimal results
resultLinks = []                # Stores all links of optimal results

# For Reference: # url = "https://kat.cr/usearch/" + serie + "%20s"+season + "e"+episode + "%20category%3Atv/?field=time_add&sorder=asc&rss=1"


#### Setting the `url` variable depending on wether season and episode is provided ####
if season and episode:              # Both season and episode
    url = "https://thekat.tv/usearch/" + serie + "%20s"+season + "e"+episode + "%20category%3Atv/?field=time_add&sorder=asc&rss=1"
if not season and episode:          # Only episode
    print("For better results, include season. Returning episode of the latest season.")
    url = "https://thekat.tv/usearch/" + serie + "%20e"+episode + "%20category%3Atv/?field=time_add&sorder=desc&rss=1"
if not episode and season:          # Only season
    print("For better results, include episode. Returning latest episode of the season.")
    url = "https://thekat.tv/usearch/" + serie + "%20s"+season + "%20category%3Atv/?field=time_add&sorder=desc&rss=1"
if not season and not episode:      # No episode or season
    print("Providing latest result only. Not really accurate.")
    url = "https://kat.cr/usearch/" + serie + "%20category%3Atv/?field=time_add&sorder=desc&rss=1"

# Print url for fun.
print(url)


#### Make the request
rssdata = feedparser.parse(url)

for index in range(len(rssdata["entries"])):                                        # For every entry of result
    size = int(rssdata["entries"][index]["torrent_contentlength"])/1024/1024        # Set size
    title = rssdata["entries"][index]["title"]                                      # Set title
    link = rssdata["entries"][index]["links"][0]["href"]                            # Set link
    if size < 500:                                                                  # Continue with entry only if size < 500 MB
        if 'LOL' in title or 'ettv' in title or 'rartv' in title:                   # Make sure the title is reputable. The keywords help.
            print(str(round(size)), " - ", title, " (", link, ")")                          # List all good results when script runs
            resultSizes.append(size)                                                # Store size of entry
            resultTitles.append(title)                                              # Store title of entry
            resultLinks.append(link)                                                # Store link of entry
            counter += 1                                                            # Increment counter as good result.

print("Count: ", counter)

if counter > 0:                                                                     # If at least 1 good result
    command = "python send_message.py \""+resultLinks[0]+"\""  # Set var "python hangupsapi/examples/send_message.py <oldest link>"
    print("Sending hangouts message: ", command)
    os.system(command)                                                              # Run the command to send hangouts message.
    f = open("data.js", "r+")
    jsondata = json.loads(f.read())
    print("script.py::jsondata", jsondata)
    for i in range(len(jsondata)):
        print("script.py::jsondata[i]['serie']::", jsondata[i]["serie"])
        if jsondata[i]["serie"] == urllib.parse.unquote(serie):
            print("removed: ", jsondata[i]["serie"])
            jsondata.pop(i)
            break
    f.close()
    f = open("data.js", "w+")
    f.write(json.dumps(jsondata))
    f.close()
