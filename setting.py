import os

# 봇 기본정보
token = os.environ['Token'] # 봇의 토큰
owner = os.environ['Owner'] # 봇 소유자

# 공공데이터 API
covid19APIkey = os.environ['Covidkey'] # 코로나19 API키
weatherAPIkey = "" # 기상청 API키

# 네이버 API
NaverAPIID = os.environ['NaverID']
NaverAPIPW = os.environ['NaverPW']

RiotAPIKey = os.environ['Riotkey']