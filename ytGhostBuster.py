#!/usr/bin/python

import urllib.request
import json
import os
import itertools
import re

API_KEY="" # TODO: get from console.google.com
VIDSBASE='{}/Videos/YouTubes/'.format(os.path.expanduser("~")) # TODO: set where all vids will be saved

channels=[
    "UC7SeFWZYFmsm1tqWxfuOTPQ", # dankula
    "UCwW_vaMPlq8J4weKDsfeJzw", # Bearing
    "UC-yewGHQbNFpDrGM0diZOLA", # Sargon
    "UCpiCH7qvGVlzMOqy3dncA5Q", # The Thinkery
    "UCx_SEanFxmYdkylVM1v3RDg", # The Incredible Salt Mine
    "UCDc_MCu3ZstNXmAqqT36SNA", # Sugartits
    "UC-EREEErQQqgYNyNB4YGQnQ", # Patrick
    "UCG749Dj4V2fKa143f8sE60Q", # Tim Pool
]

################################################################################
# Probably no need to change anything below
################################################################################
COUNT="5" # TODO: tune me if desired

archive = '{}/archive.txt'.format(VIDSBASE)
youtubedlopts='{}/%(uploader)s/%(upload_date)s - %(id)s - %(title)s.%(ext)s'.format(VIDSBASE)

################################################################################
# Very little need to change anything below...
################################################################################

vidlist=[] # list of all video urls to fetch

def get_videos_in_channel(channel_id,maxResults):
    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults={}'.format(API_KEY, channel_id,maxResults)

    video_links = []
    url = first_url

    with urllib.request.urlopen(url) as url:
        inp = url.read()
    resp = json.loads(inp.decode("utf-8"))

    for i in resp['items']:
        if i['id']['kind'] == "youtube#video":
            video_links.append(base_video_url + i['id']['videoId'])

    return video_links

def get_vid(url):
    m = re.search('.*watch\?v=(.*)', url)
    if m:
        return m.group(1)

def check_archive(vid):
    return open(archive,'r').read().find(vid) >= 0


for chan in channels:
    vidlist.extend(get_videos_in_channel(chan,COUNT))

for url in vidlist:
    if check_archive(get_vid(url)) == False :
        cmdstring = 'youtube-dl --download-archive {} -f best --write-info-json -o \'{}\' "{}"'.format(archive,youtubedlopts,url)
        #os.system(cmdstring)
        print(cmdstring)
