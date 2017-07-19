#!/usr/bin/env python3
from urllib.request import urlopen, Request
import feedparser
import html
import re
import leetx

def main():
	print("Bye")



def escape(query):
	return(query.replace(" ","%20"))

def search(query,ep):
	eps = query.replace("(ep)",epsf(ep))
	return leetx.search(eps)[0]



def search_gen(query,n1=3,n2=1):
	results = leetx.search(query,n1)
	print(results)
	rep={}
	j=0
	l = len(results)
	for i in range(l):
		rep[j] = results[j]
		j+=1
	return rep


#n1 - is terminal max and n2 is number of viable results
#def search_gen(query,n1,n2):
#	rep = {}
#	rss = feedparser.parse("https://extra.to/rss.xml?type=search&search="+escape(query))
#	#print(rss["entries"])
#	n1 = n1 if len(rss["entries"]) > n1 else len(rss["entries"])
#	j=0
#	for i in range(n1):
#		if( not (rss["entries"][i]["tags"][0]["term"].startswith("Adult"))):
#			j+=1
#			rep[j] = {rss["entries"][i]["title"]:rss["entries"][i]["magneturi"]}
#		if(j>n2):
#			break;
#	return(rep)
#	#return str

# Formatting numbers:
def epsf(ep):
	m = re.search('[sS](\d{1,2})[Ee](\d{1,2})', ep)
	season, episode = m.group(1).zfill(2), m.group(2).zfill(2)
	# rep - Rebuilt episode number
	rep = "S" + season + "E" + episode
	return(rep)


if __name__ == '__main__':
	main()
else:
	print("[leetx_search]:loaded")
