# Ex03_json_exam.py

'''
    data / sample.json 파일을 읽고 총합 구해서 출력
'''

f = open('./data/sample.json', 'rt', encoding='utf-8')
data = f.read()
f.close()

import json
items = json.loads(data)

sum = 0
for k,val in items.items():
    print(k, '>>', val['price'] * val['count'])
    sum += (val['price'] * val['count'])
print(sum)