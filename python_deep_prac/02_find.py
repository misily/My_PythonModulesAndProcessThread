text = ('Make America Great Again')

print('1번 경우: ',text.find('i'))
print('2번 경우: ',text.find('i', 9, 15))
print('3번 경우: ',text.find('i', 11, 15))

# 3번 경우 문자열의 11번째 15번째 사이에 'i'가 없어서 -1을 반환