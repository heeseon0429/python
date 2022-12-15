import cx_Oracle as oci

# 1. Connection 얻어오기
conn = oci.connect('scott/tiger@127.0.0.1:1521/xe')
print(conn.version)
# 2. sql 문장
sql = 'select * from emp'
# 3. cursor 객체 얻어오기
cursor = conn.cursor()
# 4. 실행
cursor.execute(sql)
datas = cursor.fetchall()
for row in datas:
    print(row[0],row[1])
# 5. cursor 객체 닫기
cursor.close()
# 6. Connection 닫기
conn.close()
