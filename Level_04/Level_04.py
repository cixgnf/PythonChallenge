import requests
import re
import time

def geturl(url, payload):
    ry = requests.Session()
    
    headers = {'Accept' : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            'Accept-Encoding' : "gzip, deflate",
            'Accept-Language' : "zh-CN,zh;q=0.9",
            'Connection' : "keep-alive",
            'Host' : "www.pythonchallenge.com",
            'Referer' : "http://www.pythonchallenge.com/pc/def/linkedlist.php",
            'Upgrade-Insecure-Requests' : "1",
            'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'"
            }
    
    status = ry.get(url, params=payload, headers=headers).text
    return status
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
payload = {'nothing': '12345'}
i = 0
while payload['nothing'] != 'peak.html' :
    try :
        str0 = geturl(url, payload)
        print(i, payload['nothing'], str0)
        payload['nothing'] = str0.split(' ')[-1]
    except Exception as e:
        print(i, 'NetWork ERR, retry!')
    #         print(repr(e))
    #         time.sleep(1)
    i += 1