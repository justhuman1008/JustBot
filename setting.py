import os

# 봇 기본정보
token = os.environ['Token'] # 봇의 토큰
guild = int(os.environ['Guild']) # 테스트용(관리자 전용) 길드
owner = os.environ['Owner'] # 봇 소유자


# API키
NaverAPIID = os.environ['NaverID']
NaverAPIPW = os.environ['NaverPW']

covid19APIkey = os.environ['Covidkey']

RiotAPIKey = os.environ['Riotkey']

#봇 공통사항----------------------------------------------------------------------------------------------
'''
아래 내용은 가급적 기본으로 두는것을 추천합니다.
'''

hcs_path ="hcs_info.json"