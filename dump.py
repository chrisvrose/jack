import feedparser

url = "https://kat.cr/usearch/blacklist%20s03%20category%3Atv/?field=time_add&sorder=desc&rss=1"

rssdata = feedparser.parse(url)
print rssdata