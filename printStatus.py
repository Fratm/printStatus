#!/usr/bin/python3
import requests
import json
from datetime import datetime

now = datetime.now()
fulldate = now.strftime("%d/%m/%Y %H:%M:%S")

#Variables for api call
apiUrlBase = "http://octopi.lan/api/job"
apikey = "PUT YOUR API KEY HERE"
headers = {'Content-Tye': 'application/json','Authorization': 'Bearer {0}'.format(apikey)}

print ("\033c")
print ("---------------------------------------")
print ("\t", fulldate)
print ("---------------------------------------")

def getInfo():
    api_url = apiUrlBase
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content)
        #return json.loads(response.content.decod('utf-8'))
    else:
        return None


printinfo = getInfo()

if printinfo is not None:
    for k,v in printinfo.items():
        print ("{0}".format(k))
        if isinstance(v, dict):
            for a,b in v.items():
                print("\t", a , ":",b)
