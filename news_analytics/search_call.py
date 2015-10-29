__author__ = 'sambhav'

import json
import Fetch2json as fj

def getNews(val):

   fj.writeTojson(val)
   with open("fetch.json") as f:
   	res = json.load(f)
   return res
