text = ['Make', 'America','Great', 'Again']

del text[1]
# del 은 함수가 아니라 예약어 그래서 함수와 같이 사용할 수 없다.

print(text)


text = ['Make', 'America','Great', 'Again']

del text[1:]

print(text)


text = ['Make', 'America','Great', 'Again']

del text[:1]

print(text)
