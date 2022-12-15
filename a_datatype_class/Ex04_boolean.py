# 부울형 - 첫글자는 반드시 대문자 True, False, None 여야 한다
t = True
f = False
n = None    # 다른 언어의  null 값과 유사

hungry = True
sleepy = False
print(not hungry)           #False
print(hungry and sleepy)    #False
print(hungry or sleepy)     #True
print(hungry & sleepy)      #False
print(hungry | sleepy)      #True





"""
        자료형         값           부울형
    -----------------------------------------------------
        문자형       "문자"          True
                    ""                     False
        리스트       [1,2,3]         True       
                    []                     False
        튜플         ()                     False
        딕셔너리     {}                     False
        숫자형       0이아닌 숫자     True
                    0                      False
                    None                   False


"""
print('-------------------')
if '희선':
    print('True')
else:
    print('False')

if []:
    print('True2')
else:
    print('False2')

if 0:
    print('True3')
else:
    print('False3')

if -1:    # 0이 아닌 숫자 True / -1도 값이 있기 때문에 True
    print('True4')
else:
    print('False4')

print('------------------')
msg = '행복합시다'
if(msg.find('행')):      # '행'은 index 0이기 때문에 [ no ] / '복'은 index 1이기 때문에 [ ok ]
    print('ok')
else:
    print('no')

if(msg.find('행') > -1):      #
    print('ok')
else:
    print('no')

if(msg.find('가')):      # '가'는 없는 값이기 때문에 -1로 return [ ok ]
    print('ok')
else:
    print('no')

if(msg.find('가')>0):
    print('ok')
else:
    print('no')

print('--------------------')