
'''
from bs4 import BeautifulSoup
from urllib import request

# yes24 > '파이썬' 검색
html = request.urlopen("https://search.kyobobook.co.kr/search?keyword=python&gbCode=TOT&target=total")
soup = BeautifulSoup(html, 'html.parser')

info = soup.select('li.prod_item')
for i in info:
    imgTag = i.select('img')
    print(imgTag)
    #print(imgTag[0].attrs['src'])
'''

print('-----')
from selenium import webdriver
from urllib import request
# chrome의 ...을 눌러 크롬버전을 본다
# chrome driver를 버전에 맞게 다운로드 : https://chromedriver.chromium.org/downloads
## Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome('../4_selenium_class/webdriver/chromedriver.exe')
driver.get('https://search.kyobobook.co.kr/search?keyword=python&gbCode=TOT&target=total')
info = driver.find_elements_by_class_name('prod_img_load')
info2= driver.find_elements_by_class_name('result_checkbox.spec_checkbox')
for x,y in zip(info,info2):
    print(y.get_attribute('data-name'),' : ', x.get_attribute('src'))
    request.urlretrieve(x.get_attribute('src'),'imgs/' + y.get_attribute('data-name').strip().replace('/','_') + '.jpg')
driver.close()