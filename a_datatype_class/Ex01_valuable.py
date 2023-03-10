"""
    파이션  - 무료이지만 강력하다
        ` 만들고자 하는 대부분의 프로그램 가능
        ` 물론, 하드웨어 제어같은 복잡하고 반복 연산이 많은 프로그램은 부적절
        ` 그러나, 다른언어 프로그램을 파이썬에 포함 가능 
        
    [주의] 줄을 맞추지 않으면 실행 안됨

    [실행] Run 메뉴를 클릭하거나 단축키로 shift + ctrl + F10

    [도움말] ctrl + q

"""

""" 
여러줄 주석 """
'''
여러줄 
주석인가??'''
# 한줄 주석

# 문자열표시
print("헬"
      "로우")
print('hello')

print("""안
녕""")
print('''
    올
    라
    ''')
# 실행 : shift + ctrl + F10

'''
[참고] 자바의 변수
    int a = 10;
    
변수란 
    파이션의 모든 자료형은 객체로 취급한다(파이선은 참조형 변수)
    a = 7
            7 객체을 가리키는 변수 a이다. ( 저장한다는 표현 안함 )
            변수 a는 7이라는 정수형 객체를 가리키는 레퍼런스이다.
            여기서 7은 기존 프로그램언어에 말하는 상수가 아닌 하나의 객체이다.
    
    [변수명 규칙]
    - 영문자 + 숫자 + _ 조합
    - 첫글자에 숫자는 안됨
    - 대소문자 구별
    - 길이 제한 없음
    - 예약어 사용 안됨       
'''
import keyword
print(keyword.kwlist)
# 자바 int a = 7;
a = 7
b = 7
c = 8
print(type(a))
print(id(a))
print(id(b))
print(id(c))
print(id(7))
print(id(8))

# 여러 변수 선언
a, b = 5, 10
print('a+b=', a+b)  # a+b = 15 # python style
# print('a+b=' +(a+b))          # java style

# 두 변수의 값을 서로 교환(swap)
'''
a = 10
b = 20

temp = a
a = b
b = temp  #값을 맞교환할 때 삼각형 구조로 만들어 줘야함
'''
a, b = 10, 20
a, b = b, a
print('A=', a, "B=", b)

# new <-> del (delete)
del b
print('A=', a, ", B=", b)  # b를 지웠기 떄문에 오류


