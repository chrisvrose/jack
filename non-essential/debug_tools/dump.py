#!python3
## dump.py (optional)
## Playing around with kat.cr rss feeds. Just dumps the results in output.

import feedparser
import requests

url = "https://proxy-nl.hide.me/go.php?u=https%3A%2F%2Fthekat.tv%2Fusearch%2FArrow%2520s04e20%2520category%253Atv%2F%3Ffield%3Dtime_add%26sorder%3Dasc%26rss%3D1&b=4"

rssdata = feedparser.parse(url)
print(rssdata)

print("REQUEST:")
print( requests.get(url, headers={'referer': 'https://proxy-nl.hide.me/go.php?u=https%3A%2F%2Fkat.cr%2F&b=4'} ).text )