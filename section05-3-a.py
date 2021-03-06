# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 = fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

# 풀이 1
print(''.join([q1[s] for s in q1 if s == '가을']))

# 풀이 2
for k in q1.keys():
    if k == '가을':
        print(q1[k])

# 풀이 3
for k,v in q1.items():
    if k == '가을':
        print(v)

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.

q2 = fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

# 풀이 1
hasApple = ['사과다!' for key, val in q2.items() if key == '사과' or val == '사과']

if len(hasApple) > 0:
    print('사과 있음')
else:
    print('사과 없음 ㅡㅡ')

# 풀이 2
for k, v in q2.items():
    if v == '사과':
        print('사과 있음')
        break
else:
    print('사과 없음')


# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

score = 100
grade = ''
if 0 < score > 100:
    grade = '나가'
elif score > 80:
    grade = 'A'
elif score > 60:
    grade = 'B'
elif score > 40:
    grade = 'C'
elif score > 20:
    grade = 'D'
elif score >= 0:
    grade = 'E'

print(grade)


# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18

a = 12
b = 6
c = 18
best = 0

best = a
if b > a:
    best = b
if c > b:
    best = c

print(best)


# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)

s = '891022-2473837'
if int(s[7]) % 2 == 0:
    print('여자')
else:
    print('남자')


# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]

# 풀이 1
print(''.join([s for s in q3 if s != '정']))

# 풀이 2
for v in q3:
    if v == '정':
        continue
    else:
        print(v)

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.

# 풀이 1
print(' '.join([str(s) for s in range(1, 100) if int(s) % 2 == 1]))

# 풀이 2
for n in range(1, 101):
    if n % 2 != 0:
        print(n, end=' ')

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

# 풀이 1
print([s for s in q4 if len(s) >= 5])

# 풀이 2
for v in q4:
    if len(v) >= 5:
        print(v)

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

# 풀이 1
print([s for s in q5 if s.islower()])

# 풀이 2
for v in q5:
    if v.isupper():
        continue
    else:
        print(v)

# 풀이 3
for v in q5:
    if v.islower():
        print(v)

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

# 풀이 1
print([s.upper() if s.islower() else s.lower() for s in q5])

# 풀이 2
for v in q6:
    if v.isupper():
        print(v.lower())
    else:
        print(v.upper())
