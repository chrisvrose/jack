#!python3
## dump.py (optional)
## Playing around with kat.cr rss feeds. Just dumps the results in output.

import feedparser

url = "https://thekat.tv/usearch/The%20Flash%20s02e20%20category%3Atv/?field=time_add&sorder=asc&rss=1"

rssdata = feedparser.parse(url)
print(rssdata)