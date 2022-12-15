"""
 [ 제어문 ]
    - 파이썬은 들여쓰기를 하여 블록{}을 대신 표현한다
    - 들여쓰기는 탭과 공백을 섞어 쓰지 말자 ( 무조건 탭만 / 1탭 : 4스페이스)
{
    int a = 10;
    int b = 20;

}
    [ex]
    if a>b:
        print(a)
            print(b)  => 에러발생 ( 줄 맞추기 )

    (1) if 문
        if 조건식A :
            문장들
        elif 조건식B :
            문장들
        else :
            문장들

        ` 조건식이나 else 뒤에는 콜론(:) 표시
        ` 조건식을 ( ) 괄호 필요없다
        ` 실행할 코드가 없으면 pass
        ` 파이썬은 switch 문 없음
        ` : 아직 끝나지 않음을 뜻함
        ` pass 문장 마지막? 잘 모르겠네 허허
"""

# 거짓(False)의 값
i = 0;
i2 = 0.0
i3 = ""
i4 = str()
i5 = list()
i6 = tuple()
i7 = set()
i8 = dict()
i9 = {}
i10 = None

#
a = -1
if a:
    print('True')
else:
    print('False')

# a, b 둘 중에 값이 0인 아이가 있으면 and는 False
a = 5
b = 3
if a and b:
    print('True2')  # False

if a or b:
    print('True3')  # True3

print(a and b)  # b = 0 False이기 때문에  0 출력
print(a or b)  # b = 0 False이기 때문에 a 값인 -1 출력

# ------------------------------------------------
a = 20
b = 0

if a:
    c = 2
elif b:
    c = 4
else:
    c = 6

print(c)
