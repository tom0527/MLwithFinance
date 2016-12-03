import urllib.request
import urllib.parse
import json

def getrate():
    currlist = ["USDJPY","USDEUR","USDGBP","EURJPY","EURGBP","GBPJPY"]

    #could be more efficient with lists

    ask = [None]*len(currlist)
    bid = [None]*len(currlist)
    rate = [None]*len(currlist)
    rateid = [None]*len(currlist)
    created = [None]*len(currlist)

    for  i in range(0, len(currlist)):
        curr = currlist[i]
        url = "https://query.yahooapis.com/v1/public/yql"
        params = {
            "q": 'select * from yahoo.finance.xchange where pair in ("'+curr+'")',
            "format": "json",
            "env": "store://datatables.org/alltableswithkeys"
        }
        url += "?" + urllib.parse.urlencode(params)
        res = urllib.request.urlopen(url)

        result = json.loads(res.read().decode('utf-8'))
        ask[i] = result["query"]["results"]["rate"]["Ask"]
        bid[i] = result["query"]["results"]["rate"]["Bid"]
        rate[i] = result["query"]["results"]["rate"]["Rate"]
        rateid[i] = result["query"]["results"]["rate"]["id"]
        created[i] = result["query"]["created"]

    return (currlist,ask,bid,rate,rateid,created)
