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


def mainScript(serie, season="", episode=""):
    
    KAT_BASE = "https://thekat.tv/"
    
    #### Making sure that the serie, season and episode are not invalid ####
    if  serie == "":
        parser.error("Invalid serie (Empty Series Argument) ")
    if len(str(season)) > 2 and season != None and episode != None:
        parser.error("Season number cannot be larger than 2")
    elif season != None:
        season = '%02d' % int(season)
    if len(str(episode)) > 2 and episode != None:
        parser.error("Episode number cannot be larger than 2")
    elif episode != None:
        episode = '%02d' % int(episode)
    
    #### Printing just for fun ####
    print("Argument values:")
    print("Serie: ", serie + "\t", "Season: ", season, "\t", "Episode: ", episode)
    
    #### Init some variables that are required. ####
    counter = 0                     # Stores the number of optimal results
    resultSizes = []                # Stores all sizes of optimal results
    resultTitles = []               # Stores all titles of optimal results
    resultLinks = []                # Stores all links of optimal results
    resultMagnets = []
    
    # For Reference: # url = "https://kat.cr/usearch/" + serie + "%20s"+season + "e"+episode + "%20category%3Atv/?field=time_add&sorder=asc&rss=1"
    #### Setting the `url` variable depending on wether season and episode is provided ####
    if season and episode:              # Both season and episode
        url = KAT_BASE + "usearch/" + serie + "%20s"+season + "e"+episode + "%20category%3Atv/?field=time_add&sorder=asc&rss=1"
    if not season and episode:          # Only episode
        print("For better results, include season. Returning episode of the latest season.")
        url = KAT_BASE + "usearch/" + serie + "%20e"+episode + "%20category%3Atv/?field=time_add&sorder=desc&rss=1"
    if not episode and season:          # Only season
        print("For better results, include episode. Returning latest episode of the season.")
        url = KAT_BASE + "usearch/" + serie + "%20s"+season + "%20category%3Atv/?field=time_add&sorder=desc&rss=1"
    if not season and not episode:      # No episode or season
        print("Providing latest result only. Not really accurate.")
        url = KAT_BASE + "usearch/" + serie + "%20category%3Atv/?field=time_add&sorder=desc&rss=1"
    
    # Print url for fun.
    print(url)
    
    
    #### Make the request
    rssdata = feedparser.parse(url)
    
    for index in range(len(rssdata["entries"])):                                        # For every entry of result
        size = int(rssdata["entries"][index]["torrent_contentlength"])/1024/1024        # Set size
        title = rssdata["entries"][index]["title"]                                      # Set title
        link = rssdata["entries"][index]["links"][0]["href"]                            # Set link
        magnet = rssdata["entries"][index]["torrent_magneturi"]
        if size < 500:                                                                  # Continue with entry only if size < 500 MB
            if 'LOL' in title or 'ettv' in title or 'rartv' in title:                   # Make sure the title is reputable. The keywords help.
                print(str(round(size)), " - ", title, " (", link, ")")                          # List all good results when script runs
                resultSizes.append(size)                                                # Store size of entry
                resultTitles.append(title)                                              # Store title of entry
                resultLinks.append(link)                                                # Store link of entry
                resultMagnets.append(magnet)
                counter += 1                                                            # Increment counter as good result.
    
    print("Count: ", counter)
    
    if counter > 0:                                                                     # If at least 1 good result
        messageToSend = resultTitles[0]
        totalMessageSent += ("\n"+ messageToSend)
        os.system("python send_message.py \""+messageToSend+"\""        # Set var "python hangupsapi/examples/send_message.py <oldest link>")
        
        messageToSend = "Link: " + resultLinks[0]
        totalMessageSent += ("\n"+ messageToSend)
        os.system("python send_message.py \""+messageToSend+"\"")
        
        messageToSend = resultMagnets[0]
        totalMessageSent += ("\n"+ messageToSend)
        os.system("python send_message.py \""+messageToSend+"\"")
        
        print("Sent Hangout Message: ", totalMessageSent)        #Printing out the message that was spit out
        
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
        
    return counter


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Tose App - script.py')
    parser.add_argument('serie', type=str, help='Serie', nargs='+')
    parser.add_argument('-s', type=int, help='Season')
    parser.add_argument('-e', type=int, help='Episode')
    args = parser.parse_args()
    serie = urllib.parse.quote(' '.join(args.serie), safe='')
    
    mainScript(serie, args.s, args.e)
else:
    print("[script] ",__name__, " module loaded")