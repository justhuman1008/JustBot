import os
import sys
import urllib.request
import setting
import json

client_id = setting.NaverAPIID
client_secret = setting.NaverAPIPW
encText = urllib.parse.quote("naver.com")
data = "url=" + encText
url = "https://openapi.naver.com/v1/util/shorturl"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    res = json.loads(response_body.decode('utf-8'))
    print(res["result"]["url"])
else:
    print("Error Code:" + rescode)