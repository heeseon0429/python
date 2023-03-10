"""
@ 네이버 금융에서 환률 정보 가져오기

` 크롬에서 네이버 > 금융 > 시장지표 > 미국 USD 금액을 부분을 개발자 모드로 확인
      <div class='head_info'>
         <span class='value'>1.098.50</span>
"""

from bs4 import BeautifulSoup
from urllib import request as req
import json


# 웹 문서 가져오기
url = 'https://finance.naver.com/marketindex/'
res = req.urlopen(url)
print(res)

# 파싱하기
soup = BeautifulSoup(res, 'html.parser')

# 추출하기
usd = soup.select_one('#exchangeList span.value')
print(usd)
print('달러:', usd.text)

name = soup.select('#exchangeList li span.blind')
# names =json.loads(name)
# print(names)
hwan = soup.select('#exchangeList span.value')
print(name[0].text,':', hwan[0].text)
# print('엔화:', hwan[1].text)
# print('유로:', hwan[2].text)
# print('중국:', hwan[3].text)
