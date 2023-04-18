# remove

text = ['Make', 'America','Great', 'Again']

text.remove('Make')

print(text)

# pop

text = ['Make', 'America','Great', 'Again']

print(text.pop()) # 마지막 요소를 꺼냄
print(text) # 마지막 요소가 사라짐

# count

text = ['Make', 'America','Great','Great', 'Again']

print(text.count('Make'))
print(text.count('Great'))


#extend

text = ['Make', 'America','Great','Again']

text2 = ['by', 'Trump', 'and', 'Obama']

text.extend(text2)

print(text)