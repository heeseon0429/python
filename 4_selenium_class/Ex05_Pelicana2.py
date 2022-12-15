from selenium import webdriver
from bs4 import BeautifulSoup
import time
from urllib import parse


driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(3)
for pageno in range(1,11):
    driver.get('https://pelicana.co.kr/store/stroe_search.html?page='+str(pageno))
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    name = soup.select('#contents td:nth-child(1)')# list
    tel = soup.select('#contents td:nth-child(3)')# list
    for x, y in zip(name, tel):
        print('매장명 : ', x.text, '\n전화번호: ', y.text.strip(),'\n----------')
# 모든 매장명 전화번호


