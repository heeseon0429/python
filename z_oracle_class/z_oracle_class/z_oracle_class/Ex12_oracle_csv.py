import csv

import cx_Oracle as oci

def createDBTable():
    conn = oci.connect('scott/tiger@127.0.0.1:1521/xe')
    sql = 'CREATE TABLE supply('\
          'id number primary key,' \
          'supplier_name varchar2(50),' \
          'invoice_number varchar2(50),' \
          'part_number varchar2(30),' \
          'cost number,' \
          'purchase_date date' \
          ')'
    sql0 = "create sequence seq_supply_id"
    cursor = conn.cursor()
    cursor.execute(sql)
    cursor.execute(sql0)
    cursor.close()
    conn.close()

def saveDBTable(data):
    conn = oci.connect('scott/tiger@127.0.0.1:1521/xe')
    sql = ''' INSERT INTO SUPPLY
            VALUES(seq_supply_id.nextval, :0, :1, :2, :3, :4)
          '''
    cursor = conn.cursor()
    cursor.execute(sql,data)
    cursor.close()
    conn.commit() # 잊지 말자.!
    conn.close()

def viewDBTable(tablename):
    conn = oci.connect('scott/tiger@127.0.0.1:1521/xe')
    sql = "Select * from " + tablename
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    print("Table : ", tablename)
    for row in data:
        print(row)
    cursor.close()
    conn.commit() # 잊지 말자.!
    conn.close()
if __name__ == "__main__":
    # createDBTable()
    imsi = ['kosmo', '9999', '8888', 1000, '2022-12-24']

    # saveDBTable(imsi)

    # file = open('supply.csv', 'r')
    # data = csv.reader(file)
    # header = next(data, None)
    # print(header , '\n','-'*50)
    # for row in data:
    #     print(row)
    #     saveDBTable(row)

    viewDBTable('supply')

