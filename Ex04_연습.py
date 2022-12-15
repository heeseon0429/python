import urllib.parse

from bs4 import BeautifulSoup
from urllib import request, parse
import os
from urllib.parse import quote_plus

'''
[1]
http://www.pythonscraping.com/pages/warandpeace.html
녹색 글자만 추출하여 출력


html = request.urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
soup = BeautifulSoup(html, 'html.parser')
info = soup.select('span.green')
print('녹색 글자만 추출하여 출력')
for x in info:
    print(x.text)
'''
#--------------------------------------
'''
[2]
http://www.pythonscraping.com/pages/page3.html
아이템과 가격을 추출
'''
html = request.urlopen("http://www.pythonscraping.com/pages/page3.html")
soup = BeautifulSoup(html, 'html.parser')
info = soup.select('#giftList tr.gift td:nth-child(3)')
info2 = soup.select('#giftList tr.gift td:nth-child(1)')
for x,y in zip(info,info2):
    print( y.text.strip(), ': ',x.text.strip())

#--------------------------------------
print('-----------------------------------')
'''
[3]
https://wikidocs.net/
 1) 책 제목과 저자만 추출
 2) 이미지 다운
 '''
html = request.urlopen("https://wikidocs.net/")
soup = BeautifulSoup(html, 'html.parser')
info = soup.select('div.media a.menu_link')
info2 = soup.select('div.media a.book-subject')
for x,y in zip(info,info2):
    print(y.text, ' : ', x.text)

print('-----------------------------------')
os.makedirs('wikiImage', exist_ok=True)

url='https://wikidocs.net/'
html = request.urlopen(url)

soup = BeautifulSoup(html,'html.parser')
titles = soup.select('#books .book-subject')
author = soup.select('#books .book-detail .menu_link')
imgs = soup.select('#books .book-image')

for i in imgs:
    print(i.attrs['src'])

for t, a in zip(titles, author):
    print("책제목 : ",t.text, " - 책 저자 : ",a.text)

for i, t in zip(imgs, titles):
    try:
        request.urlretrieve(parse.urljoin(url,i.attrs['src']),'./wikiImage/{}.png'.format(t.text))
    except UnicodeEncodeError:
        i = quote_plus(parse.urljoin(url,i.attrs['src']),safe="://")
        request.urlretrieve(i,'./wikiImage/{}.png'.format(t.text))
print(len(titles))
