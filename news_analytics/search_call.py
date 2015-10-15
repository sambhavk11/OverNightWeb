__author__ = 'sambhav'


import json
import transferContent as tc

def getNews(val):
    tc.transContent(val)
    with open("dummy.json") as f:
        res = json.load(f)
    results = filter_news(res)
    return results

def filter_news(res):
    results = res.get("result").get("docs")
    return results
