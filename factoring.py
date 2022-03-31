import os
import urllib.request
from furl import furl
import json
import sys

import setting

client_id = setting.NaverAPIID
client_secret = setting.NaverAPIPW
encQuery = urllib.parse.quote("search")
data = "query=" + encQuery
url = "https://openapi.naver.com/v1/papago/detectLangs"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    res = json.loads(response_body.decode('utf-8'))
    result = res['langCode']
    print(result)
else:
    print("Error Code:" + rescode)


'''
ko = "한국어"
en = "영어"
ja = "일본어"
zh-CN = "중국어 간체"
zh-TW = "중국어 번체"
vi = "베트남어"
id = "인도네사아어"
th = "태국어"
de = "독일어"
ru = "러시아어"
es = "스페인어"
it = "이탈리아어"
fr = "프랑스어"
'''