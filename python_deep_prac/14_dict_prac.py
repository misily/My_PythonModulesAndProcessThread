dict_ = {}  # 빈 딕셔너리

dict_['score'] = 4

print(dict_)

del dict_['score']

print(dict_)

# del dict_['score'] # 키값에 밸류없으면 에러가 뜸

# print(dict_)

dict2 = {'name': 'ESKim', 'gender':'M', 'age':27}

print(dict2.keys())
print(dict2.values())

print(dict2.items())

dict2.clear()

print(dict2)

dict2 = {'name': 'ESKim', 'gender':'M', 'age':27}

dict2.get('name')
dict2.get('email')

print(dict2.get('email')) # 값이 없어서 NONE 리턴 ** 에러가 안남
print(dict2.get('name'))

if 'age' in dict2:
    print('나이 정보를 가지고 있음')