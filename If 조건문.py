# if 3 > 4 :
#     print("3은 1보다 큽니다.")
#     print("연산을 종료합니다.")
# # 들여쓰기는 Tab -> Tab 취소는 Shift + Tab
# print("-"*30)
# print("저는 들여쓰기를 하지 않은 라인입니다.")

#----------------------------------------------------------------------

# a = "임하영"
# b = "마지로"
#
# if a == b :
#     print("두 사람의 이름은 같습니다.")
#
# elif a != b :
#     print("두 사람의 이름은 다릅니다.")

#----------------------------------------------------------------------

num_1 = 10
num_2 = 3

if num_1 < num_2 :
    print("num_1은 num_2 보다 크기가 작습니다.")

elif num_1 == num_2 :
    print("num_1은 num_2 랑 크기가 같습니다.")

elif num_1 > num_2 :
    print("num_1은 num_2보다 크기가 큽니다.")

#---------------------------------------------------------------------

# and / or 연산자
apple = "사과"
banana = "감자"

# or 은 둘 중 하나만 참이여도 실행
if apple == "사과" or banana == "바나나" :
    print("문자열이 모두 정확합니다.")

var = [1,2,3]
if 3 in var :
    print("숫자 3이 var 변수에 있습니다.")

