
#import datetime
#today = datetime.date.today()
#print('today is ', today)   # today is 2022-12-05

from datetime import date, timedelta
#from datetime import timedelta
today = date.today()
print('today is ', today)   # today is 2022-12-05

# 날짜 구하기
print('년도 : ', today.year)
# 월
print('월 : ', today.month)
# 일
print('일 : ', today.day)
# 요일
print('요일 : ', today.weekday())  # 월요일 0 / JAVA, ORACLE은 일요일 0

# 날짜 계산 (음수는 표기 X)
print('어제 : ', today + timedelta(days=-1))
# 일주일 전 날짜
print('일주일 전 : ', today + timedelta(days=-7))
print('일주일 전: ', today + timedelta(weeks=-1))
# 10일 후 날짜
print('10일 후 : ', today + timedelta(days=+10))

print('-----------------')
from datetime import datetime
day = datetime.today()
print(day)

import datetime
day = datetime.datetime.today()
print(day)

#날짜를 문자열 형태 (strftime() 이용)
print(day.strftime('%Y년 %m월 %d일 %H:%M ')) # 대문자 Y : 2022년 / 소문자 y : 22년

#문자열를 날짜 형태 (strptime() 이용)
naljja = '2022-12-25 12:50:59'
print(type(naljja))
mydate = datetime.datetime.strptime(naljja, '%Y-%m-%d %H:%M:%S')
print(mydate)
print(type(mydate))
