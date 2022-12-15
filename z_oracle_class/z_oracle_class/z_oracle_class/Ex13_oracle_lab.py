"""
0. DB에 저장할 테이블 생성
1. 사용자 입력 받아 확인
2. 모든 연락처 출력하기
3. 연락처 삭제하기
"""
import cx_Oracle as oci


def make_contact_table():
    conn = oci.connect('scott/tiger@127.0.0.1:1521/xe')
    sql = '''CREATE TABLE contact(
                name varchar2(50),
                phone_name varchar2(40) primary key,
                email varchar2(100),
                addr varchar2(500)
            )'''
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


class Contact:
    def __init__(self, name, phone_number, email, addr):
        self.name = name
        self.phone_name = phone_number
        self.email = email
        self.addr = addr

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
    menu = input('메뉴선택:')
    return int(menu)


def set_contact():
    # (1)
    # 이름, 전화번호, 이메일, 주소를 입력받아
    # Contact 객체를 생성하고 DB 에 입력
    person = Contact(input('Enter 이름: '), input('Enter 전화번호: '), input('Enter 이메일: '), input('Enter 주소: '),)
    conn = oci.connect('scott/tiger@127.0.0.1:1521/xe')
    sql = "INSERT INTO CONTACT VALUES('{0}','{1}','{2}','{3}')".format(person.name, person.phone_name, person.email, person.addr)
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.commit()
        conn.close()


def print_contact():
    conn = oci.connect('scott/tiger@127.0.0.1:1521/xe')
    sql = "SELECT * from CONTACT"
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        for x in data:
            print(x)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.commit()
        conn.close()


def delete_contact(name):
    conn = oci.connect('scott/tiger@127.0.0.1:1521/xe')
    sql = "DELETE FROM CONTACT WHERE NAME = '{0}'".format(name)
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
    except Exception as e:
        print(e)
    finally:
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
    make_contact_table()
    run()
