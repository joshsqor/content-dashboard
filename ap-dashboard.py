#!/usr/bin/python
#Content Dashboard

"""
ex usage: feed_item_counts.fetch_count(item_type="AP", start_date=[2014,6,1], end_date=[2014,6,2])

valid types are:
- AP
- twitter
- instagram
- getty_images
- espn_api
- rss
- sqor
- curated
- comment

"""

from datetime import datetime
import requests
import json

URL = "http://feedtools.sqor.com/content?q=type:%(item_type)s AND published_dt:[%(start_date)s TO %(end_date)s]&limit=0"

def fetch_count(item_type, start_date, end_date=datetime.now()):
    start_date = check_date(start_date)
    end_date = check_date(end_date)
    res = requests.get(URL % { "item_type":item_type
                             , "start_date":start_date
                             , "end_date": end_date})
    print json.loads(res.content).get("total")

def check_date(adate):
    if isinstance(adate, list):
        return dater(adate[0], adate[1], adate[2])
    else:
        return isofixer(adate)

def dater(year, month, day):
    return isofixer(datetime(year, month, day))

def isofixer(adate):
    return datetime.isoformat(adate).split('.')[0] + "Z"









