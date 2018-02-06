#!/usr/bin/python

# Used to interact with the beautiful site

import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import re


class BASE(object):
    url = 'https://1337x.to'
    search = '/search/{}/1/'
    limit = 1


class Torrent(object):
    def __init__(self, title, magnet, size, seeds, leeches):
        self.title = title
        self.magnet = magnet
        self.size = size
        self.seeds = seeds
        self.leeches = leeches


# Convert gb to mb and make into float
def _gb_to_mb(size_data1):
    size_data = re.sub(",", "", size_data1);
    if size_data[-2:].lower() == 'gb':
        return float(size_data[:-3]) * 1024.0
    elif size_data[-2:].lower() == 'mb':
        return float(size_data[:-3])


def search(query,limit=BASE.limit):
    headers = {'User-Agent' : "Magic Browser"}
    req_url = BASE.url + BASE.search.format(quote_plus(query))
    #s = requests.get(req_url, headers=headers, verify=False)
    s = requests.get(req_url,headers=headers, verify=True)
    html = s.content
    soup = BeautifulSoup(html, 'html.parser')
    tbody = soup.find('tbody')
    try:
        trs = tbody.find_all('tr')
    except AttributeError as e:
        return []

    torrents = []
    index=0
    for tr in trs:
        index+=1
        link = tr.find_all('a')[1]['href']
        tds = tr.find_all('td')
        title = tds[0].text
        size_raw = tds[4].text
        m = re.search('[mM][bB]|[gG][bB]', size_raw)
        if m:
            size_split = size_raw.split(m.group())[0] + m.group()
            size = _gb_to_mb(size_split)
        else:
            size = 0
        seeds = int(re.sub(',', '', tds[1].text))
        leeches = int(re.sub(',', '', tds[2].text))

        req_url = BASE.url + link
        #s = requests.get(req_url, headers=headers, verify=False)
        s = requests.get(req_url, headers=headers, verify=True)
        html = s.content
        soup = BeautifulSoup(html, 'html.parser')
        down_ul = soup.find('ul', {'class': 'download-links-dontblock btn-wrap-list'})
        
        mag = down_ul.li.a.get('href')
        torrents.append(Torrent(title, mag, size, seeds, leeches))
        if index==limit:
            break

    return torrents
