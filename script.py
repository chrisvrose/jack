import feedparser
import urllib
import argparse
import os, sys

parser = argparse.ArgumentParser(description='Tose App')
# Serie
parser.add_argument('serie', type=str,
                    help='Serie')
# Season
parser.add_argument('-s', type=int,
                    help='Season')
# Episode
parser.add_argument('-e', type=int,
                    help='Episode')
args = parser.parse_args()

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

serie = urllib.quote(args.serie, safe='')
# season = '%02d' % args.s
# episode = '%02d' % args.e

# serie = "flash"
# season = "02"
# episode = "19"

print("Argument values:")
print("Serie: " + serie + "\t" + "Season: " + season + "\t" + "Episode: " + episode)

counter = 0
resultSizes = []
resultTitles = []
resultLinks = []

# url = "https://kat.cr/usearch/" + serie + "%20s"+season + "e"+episode + "%20category%3Atv/?field=time_add&sorder=asc&rss=1"

if season and episode:
    url = "https://kat.cr/usearch/" + serie + "%20s"+season + "e"+episode + "%20category%3Atv/?field=time_add&sorder=asc&rss=1"
if not season and episode:
    print "For better results, include season. Returning latest episode."
    url = "https://kat.cr/usearch/" + serie + "%20e"+episode + "%20category%3Atv/?field=time_add&sorder=desc&rss=1"
if not episode and season:
    print "For better results, include episode"
    url = "https://kat.cr/usearch/" + serie + "%20s"+season + "%20category%3Atv/?field=time_add&sorder=desc&rss=1"
if not season and not episode:
    print "Providing latest result only."
    url = "https://kat.cr/usearch/" + serie + "%20category%3Atv/?field=time_add&sorder=desc&rss=1"

print url

rssdata = feedparser.parse(url)
#print rssdata["entries"][0]
for index in range(len(rssdata["entries"])):
    size = int(rssdata["entries"][index]["torrent_contentlength"])/1024/1024
    title = rssdata["entries"][index]["title"]
    link = rssdata["entries"][index]["links"][0]["href"]
    if size < 500:
        if 'LOL' in title or 'ettv' in title or 'rartv' in title:
            print str(size), " - ", title, " (", link, ")"
            resultSizes.append(size)
            resultTitles.append(title)
            resultLinks.append(link)
            counter += 1

print "Count: ", counter

if counter > 0:
    command = "python3 hangupsapi/examples/send_message.py \""+resultLinks[0]+"\""
    print command
    os.system(command)


#print type(rssdata["entries"][0])