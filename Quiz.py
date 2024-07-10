## Quiz 1 : 사용자로부터 입력받은 문자열 "안녕하세요" 인 경우, 화면에 "반갑습니다." 출력

a = input("인사를 입력하세요. : ")
if a == "안녕하세요" :
    print("반갑습니다.")

## Quiz 2 : 사용자로부터 값을 입력받은 후, 해당 값에 100을 더한값을 계산. 그 후 계산한 값이 150 이상인 경우 화면에 출력하고,
## 값이 150 이하인 경우 "값이 부족합니다." 를 화면에 출력

b = input("임의의 숫자를 입력하세요. : ")
b = int(b)
c = b + 100
# class (str) = 문자열이란 뜻 / class (int) = 숫자열이란 뜻

if c > 150 :
    print(c)
elif c <= 150 :
    print("값이 부족합니다.")

## Quiz 3 : 사용자로부터 임의의 값 입력 받아서 해당 수가 5와 10 사이에 있으면 "OK"출력 그렇지 않은 경우 "NO" 출력

num = input("임의의 순자를 입력하세요. : ")
num = int(num)
if  10 > num > 5 :
    print("OK")
elif num <= 5 :
    print("NO")
elif num >= 10 :
    print("NO")
# else 는 if 조건문 빼고 나머지를 선택처리할때 사용
else :
    print("NO")

## Quiz 4 : 사용자로부터 입력 받은 단어가 아래 리스트에 포함되어 있는지 확인하라.

fruit = ["사과", "포도", "홍시"]
data = input("과일 이름을 입력해주세요. : ")
if data in fruit :
    print("정답입니다.")
else :
    print("오답입니다.")

## Quiz 5 : 딕셔너리가 정의되어 있을때 사용자가 입력한 값이 딕셔너리 키 값에 포함되었다면 "정답입니다." 아닐 경우 "오답입니다."

fruits = {"봄" : '딸기' , "여름" : '토마토' , "가을" : '사과'}
data2 = input("계절을 입력해주세요. : ")
if data2 in fruits :
    print("정답입니다.")
else :
    print("오답입니다.")

## Quiz 6 : 딕셔너리가 정의되어 있을때 value 값을 찾고싶다면

fruits2 = {"봄" : '딸기' , "여름" : '토마토' , "가을" : '사과'}
data3 = input("계절을 입력해주세요. : ")
if data3 in fruits2.values() :
    print("정답입니다.")
else :
    print("오답입니다.")

## Quiz 7 : 문자메시지 길이에 따라 문자 요금 결정되는 프로그램 작성. 메시지 길이 20 이하 50원, 20 초과 100원
## 사용자로부터 문자메시지 입력 받고 문자 요금 출력코드 작성

mes = input("문자메시지를 입력하세요. : ")
long = len(mes)
print(long)
if long <= 20 :
    print("사용하신 문자메시지 금액은 50원 입니다.")
elif long > 20 :
    print("사용하신 문자메시지 금액은 100원 입니다.")

## Quiz 8 : 점수 구간에 해당하는 학점이 아래와 같이 정의될 때. 사용자로부터 score 입력 받고 학점 환산
## 81~100 = A / 61~80 = B / 41~60 = C / 21~40 = D / 0~20 = E

score = input("점수를 입력해주세요. : ")
score = int(score)
if 81 <= score <= 100 :
    print("학점은 A 입니다.")
elif 61 <= score <= 80 :
    print("학점은 B 입니다.")
elif 41 <= score <= 60 :
    print("학점은 C 입니다.")
elif 21 <= score <= 40 :
    print("학점은 D 입니다.")
elif 0 <= score <= 20 :
    print("학점은 E 입니다.")

## Quiz 9 : 홀수 / 짝수 판독기 프로그램 작성, 사용자로부터 임의의 수 입력 받고 해당 숫자가 홀수인지 짝수인지 화면에 출력

# 1번식
num_10 = input("숫자를 입력해주세요. : ")
num_10 = int(num_10)
num_9 = num_10 % 2
if num_9 == 0 :
    print("해당 숫자는 짝수입니다.")
elif num_9 != 0 :
    print("해당 숫자는 홀수입니다.")

# 2번식
num_8 = int(input("숫자를 입력해주세요. : "))
if num_8%2 == 0 :
    print("해당 숫자는 짝수입니다.")
else :
    print("해당 숫자는 홀수입니다.")