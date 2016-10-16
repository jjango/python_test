#random
import ramdom

## radom data definition

number = [0,0,0]
number[0] = random.randrange(1,9,1)
number[1] = random.randrange(1,9,1)
while (number[0] == number[1]):
    number[1] = random.randrange(1,9,1)
while (number[0] == number[1] or number[1] == number[2] ):
    number[2] = random.randrange(1,9,1)

num_ball = 0
num_strike = 0
num_out = 0

## rotation before 3 strike
while (num_strike < 3) :
# 3 number --> save
# insert : a, b, c data (문자열 비교 -->  array  형태 저장)
input_num = input("number 3digit : ")

# check 3 number in array  matche
# strike --> order , number matches
# ball --> number only matches
# out --> all unmatch
### compare 방식 --> for 문 2회 수행 (list 의 위치 숫자 비교)
for i in range(0, 3):
    for j in range(0, 3):
        if(num[i] == str(rn[j]) and i == j):
            s_cnt += 1
        elif(num[i] == str(rn[j]) and i != j):
            b_cnt += 1
            print("결과 : [", s_cnt, "] Strike [", b_cnt, "] Ball")
t_cnt += 1
print("---------------------------")
print(t_cnt, "번 만에 정답을 맞추셨습니다.")
