
# ------------------------------------------------------
"""
   (2) for문
        for <타켓변수> in 집합객체 :
            문장들
        else:
            문장들

        ` 반복문 뒤에 else는 반복하는 조건에 만족하지않으면 실행

   (3) while 문
        while 조건문 :
            문장들
        else :
            문장들

"""
a = 112                  # 숫자형
b = ['1','2','3']        # 리스트
c = '987'                # 문자열
#d = tuple(b)             # 튜플
#d = tuple(['1','2','3']) # 튜플
d = ('1','2','3')        # 튜플
e = dict(k=5, j=6)       # 딕셔너리

# a는 반복이 안되지만 b부터 e까지는 반복된다.
for entry in e:
    print(entry)

# 딕셔러니인 경우
for entry in e:
    print(e[entry])
else:
    print('end')

# 1부터 10까지의 합 구하기
'''
for( int i=1; i <= 10; i++ ){
    sum += i;
}

for <타켓변수> in 집합객체 :
                문장들
'''
# (1)
sum = 0
for i in range(1, 11):
    sum += i
print('sum =', sum)

# (2) 1부터 10까지의 홀수의 합 구하기
sum = 0
for i in range(1, 11, 2):  # 1, 3, 5, 7, 9
    sum += i
print('sum =', sum)


"""
[과제] 2단부터 9단까지 이중 반복문으로 출력
"""
for i in range(2, 10):  # 단
    print(i, "단")
    for h in range(1,10):
        print(i, " x ", h ," = " , i*h)

# pop이 없으면 무한루프
li = ['z', 'y', 'x']
while li:
    data = li.pop()
    print(data)
else:
    print('end')
