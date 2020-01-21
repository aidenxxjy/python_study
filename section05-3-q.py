# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
if '가을' in q1:
    print(q1['가을'])

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

if q2.values() == '사과':
    print('OK')

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

score = 78
if score >= 81 and score <= 100:
    print('A학점')
elif score >= 61:
    print('B학점')
elif score >= 41:
    print('C학점')
elif score >= 21:
    print('D학점')
else:
    print('E학점')

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18

num = [12, 6, 18]
biggest_num = num[0]

if biggest_num >= num[1]:
    if biggest_num >= num[2]:
        biggest_num = num[0]
        print(biggest_num)
    else:
        biggest_num = num[2]
        print(biggest_num)
else:
    biggest_num = num[1]
    if biggest_num >= num[2]:
        biggest_num = num[1]
        print(biggest_num)
    else:
        biggest_num = num[2]
        print(biggest_num)
    
# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
num = '911111-2234567'
if num[7] == '1':
    print('남자입니다.')
elif num[7] == '3':
    print('남자입니다.')
elif num[7] == '2':
    print('여자입니다.')
elif num[7] == '4':
    print('여자입니다.')
else:
    print('주민등록번호를 제대로 입력해주세요.')

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]

for str in q3:
    if str == '정':
        break
    print(str)

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
a = [x for x in range(1,101,2)]
print(a)

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

for str in q4:
    if len(str) >= 5:
        print(str)

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for str in q5:
    if str.islower() == True:
        print(str)

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for str in q6:
    if str.islower() == True:
        print(str.upper())
    else:
        print(str.lower())
