text = ['Make', 'America','Great', 'Again']

text.sort()

print(text)

text = ['Make', 'America','Great', 'Again']

sorted(text)

print(sorted(text))
print(text)


# ---------------------------------------------
numbers = [1, 3, 4, 2, 1, 5]

def multi(num):
    return num%5  # 5로 나눈 나머지를 리턴

numbers.sort(key=multi,reverse=True)

# 5로 나눈 나머지가 큰 순서대로 정렬

print(numbers)