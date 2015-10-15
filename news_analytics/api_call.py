import requests
import json

def getNews(val):
    url = "https://access.alchemyapi.com/calls/data/GetNews"
    payload = {
      "apikey": "5dba717b7023546440cf197726069f03b50b751d",
      "return": "enriched.url.title,enriched.url.url,enriched.url.author,enriched.url.publicationDate,enriched.url.entities,enriched.url.docSentiment,enriched.url.concepts,enriched.url.taxonomy",
      "start" : "1432512000",
      "end": "1433199600",
      "q.enriched.url.text": val,
      "count": 25,
      "outputMode": "json"
    }
    #res = requests.get(url,params=payload)
    #with open("dummy.json", 'w') as f:
    #     f.write(res.text)
    #title = filter_news(res.json())

    #temporary reading
    with open("dummy.json") as f:
        res = json.load(f)
    # res = json.dumps(rest, indent=4, sort_keys=True)
    results = filter_news(res)
    return results

def filter_news(res):
    title = []
    # for eachDoc in res.get("result").get("docs"):
        # if eachDoc.get("source").get("enriched").get("url").get("title") != "":
        #     title.append(eachDoc.get("source").get("enriched").get("url").get("title"))
        # if eachDoc.get("source").get("enriched").get("url").get("title")
    results = res.get("result").get("docs")
    return results

#getNews("Aston Martin")
