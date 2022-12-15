from selenium import webdriver
from bs4 import BeautifulSoup
import cx_Oracle

driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(3)
conn = cx_Oracle.connect('scott', 'tiger', 'localhost/xe')
cursor = conn.cursor()
try:
    cursor.execute('''
    CREATE TABLE jadam(
    name varchar2(100) primary key,
    tel varchar2(30),
    addr varchar2(100),
    latitude number,
    longitude number
    )
    ''')
except:
    print('Tables is already Created.')
f = open('./jadam.txt', 'w')
f.write("매장명,전화번호,주소\n")

for pageno in range(1,75):
    driver.get('http://www.ejadam.co.kr/bbs/board.php?bo_table=store&page='+str(pageno))
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    name = soup.select('#fboardlist td:nth-child(1)')# list
    tel = soup.select('#fboardlist td:nth-child(2)')# list
    addr = soup.select('#fboardlist td:nth-child(3)')
    for x, y, z in zip(name, tel, addr):
        print('매장명 : ', x.text.strip(), '\n전화번호: ', y.text.strip(),'\n주소: ',z.text.strip(), '\n----------')
        f.writelines(x.text.strip() + ',' + y.text.strip() + ',' + z.text.strip()+'\n')
        sql = "INSERT INTO jadam(name, tel, addr) VALUES('" +x.text.strip()+"', '" + y.text.strip() + "','" + z.text.strip()+"' )"

        print(sql)
        cursor.execute(sql)

conn.commit()
f.close()
