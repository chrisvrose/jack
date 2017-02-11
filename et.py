#!/usr/bin/env python3
from urllib.request import urlopen, Request
import feedparser
import html
import re

def main():
	print("Bye")


def search(query,ep):
	# eps - episode search text
	eps = html.escape(query.replace("(ep)",epsf(ep)))
	#print(eps)
	rss = feedparser.parse("https://extratorrent.cc/rss.xml?type=search&search="+eps)
	#link = rss["entries"][0]["links"][0]["href"].replace("http://","https://")
	mgn = rss
	#mgn = ttom(link)
	#print("Found:",mgn)
	# No entries found
	if not mgn["entries"]:
		return("Not found. Sorry")
	else:
		return(mgn["entries"][0]["magneturi"])

def search_gen(query,number):
	rep = {}
	rss = feedparser.parse("https://extratorrent.cc/rss.xml?type=search&search="+query)
	number = number if len(rss["entries"]) > number else len(rss["entries"])
	for i in range(number):
		if(rss["entries"][i]["tags"][0]["term"].startswith("Adult")):
			rep[i] = {"NSFW. Ignoring.":""}
		else:
			rep[i] = {rss["entries"][i]["title"]:rss["entries"][i]["magneturi"]}
	return(rep)
	#return str

# Formatting numbers:
def epsf(ep):
	m = re.search('[sS](\d{1,2})[Ee](\d{1,2})', ep)
	season, episode = m.group(1).zfill(2), m.group(2).zfill(2)
	# rep - Rebuilt episode number
	rep = "S" + season + "E" + episode
	return(rep)

#def ttom(link):
#	details = urlopen(Request(link, headers={'User-Agent': 'Mozilla'})).read().decode()
#	if not details:
#		return ''
#	#match = re.search(r'href="(magnet:\?*)"', details)
#	match = re.search(r'(href=\"magnet:.*nce\") title=\"Magnet link\"', details)
#	if not match:
#		return ''
#	# Removing href and return
#	return match.group(1).replace("href=\"","").replace("\"","")


if __name__ == '__main__':
	main()
else:
	print("[ettv_search]:loaded")
