# (실습) 1~1000까지의 5의 배수 누적합, 7의 배수 누적합 구하기

sum5 = 0
sum7 = 0
for i in range(1, 1001):
    if i%5 == 0:
        sum5 +=i
    if i%7 == 0:
        sum7 +=i

print("5의 배수 누적함 : ", sum5)
print("7의 배수 누적합 : ", sum7)