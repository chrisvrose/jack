#!/usr/bin/env python3
from urllib.request import urlopen, Request
import feedparser
import html
import re

def main():
	print("Bye")


def search(query,ep):
	eps = html.escape(query.replace("(ep)",ep.upper()))
	print(eps)
	rss = feedparser.parse("https://extratorrent.cc/rss.xml?type=search&search="+eps)
	link = rss["entries"][0]["links"][0]["href"].replace("http://","https://")
	mgn = ttom(link)
	print("Found:",mgn)
	return(mgn)


def ttom(link):
	details = urlopen(Request(link, headers={'User-Agent': 'Mozilla'})).read().decode()
	if not details:
		return ''
	#match = re.search(r'href="(magnet:\?*)"', details)
	match = re.search(r'(href=\"magnet:.*nce\") title=\"Magnet link\"', details)
	if not match:
		return ''
	# Removing href and return
	return match.group(1).replace("href=\"","").replace("\"","")


if __name__ == '__main__':
	main()
else:
	print("[ettv_search]:loaded")