from selenium import webdriver
import cx_Oracle
from geopy.geocoders import Nominatim
geo_local = Nominatim(user_agent='South Korea')


# 위도, 경도 반환하는 함수
def geocoding(address):
    try:
        geo = geo_local.geocode(address)
        xy = [geo.latitude, geo.longitude]
        return str(xy[0]), str(xy[1])
    except:
        return "0", "0"


driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(3)
conn = cx_Oracle.connect('scott', 'tiger', 'localhost/xe')
cursor = conn.cursor()
sql = 'SELECT * FROM jadam'
cursor.execute(sql)
list = cursor.fetchall()

for x in list:
    addr = x[2]
    latitude, longitude = geocoding(addr)
    sql = "UPDATE jadam set latitude = '"+latitude+"' where addr = '" + x[2] + "'"
    sql2 = "UPDATE jadam set longitude="+longitude+" where addr = '" + x[2] + "'"
    cursor.execute(sql)
    cursor.execute(sql2)
    conn.commit()
    '''
    cursor.execute(sql2)'''
conn.close()