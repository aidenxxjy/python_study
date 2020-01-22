# Section05-4
# List Comprehension

# 1부터 100까지 list에 넣고 싶다면

# 일반적인 방법1(노가다)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, ..., 100]

# 일반적인 방법2
numbers = []

for n in range(1,101):
    numbers.append(n)
print(numbers)

# List Comprehension

numbers2 = [x for x in range(1,101)]
print(numbers2)

# [append할 변수 for 반복되는 변수 in iterable if 조건문]의 형태

