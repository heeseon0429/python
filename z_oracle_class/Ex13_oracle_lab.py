import cx_Oracle as oci
import csv
"""
0. DB에 저장할 테이블 생성
1. 사용자 입력 받아 확인
2. 모든 연락처 출력하기
3. 연락처 삭제하기
"""
class Contact:
    def __init__(self, name, phone_number, email, addr):
        self.name=name
        self.phone_name=phone_number
        self.email=email
        self.addr=addr

    def print_info(self):
        print("이름:", self.name)
        print("전화번호:", self.phone_name)
        print("이메일:", self.email)
        print("주소;", self.addr)


def print_menu():
    print('1. 연락처 입력')
    print('2. 연락처 출력')
    print('3. 연락처 삭제')
    print('4. 종료')
    menu=input('메뉴선택:')
    return int(menu)

def set_contact():
    # (1)
    # 이름, 전화번호, 이메일, 주소를 입력받아
    # Contact 객체를 생성하고 DB 에 입력

    name = input('이름은? : ')
    phone_name = input('번호 : ')
    email = input('이메일 : ')
    addr = input('주소 : ')


    contact = Contact(name, phone_name, email, addr)


    conn = oci.connect('scott/tiger@192.168.0.59:1521/xe')
    sql = "INSERT INTO hs (NAME,TEL,EMAIL,ADDR) VALUES('{0}','{1}','{2}','{3}')".format(contact.name,contact.phone_name,contact.email,contact.addr)
    cursor = conn.cursor()
    cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()



def print_contact():
    # (2)
    #  테이블의 전체 레코드 출력
    conn = oci.connect('scott/tiger@192.168.0.59:1521/xe')
    sql = '''
              select * from hs 

           '''
    cursor = conn.cursor()
    cursor.execute(sql)
    datas = cursor.fetchall()
    # print(datas)

    for row in datas:
        print(row[0], row[1], row[2],row[3])
    cursor.close()
    conn.commit()
    conn.close()

def delete_contact(name):
    conn = oci.connect('scott/tiger@192.168.0.59:1521/xe')
    sql = "DELETE from HS where name = '{0}' ".format(name)
    cursor = conn.cursor()
    cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()

def run():
    while True:
        menu=print_menu()
        if menu==4:  # 종료를 선택하면
            break
        elif menu==1: # 입력을 선택하면
            set_contact()
        elif menu==2: # 출력을 선택하면
            print_contact()
        elif menu==3: # 삭제를 선택하면
            name = input('삭제할 이름은?')
            delete_contact(name)


if __name__ == "__main__":
    run()


