# 1~1000까지의 3의 배수의 개수, 5의 배수의 개수 구하기

cnt3 = 0
cnt5 = 0
for i in range(1, 1001, 1):
    if i%3 == 0:
        cnt3 +=1  # cnt3 = cnt3 + 1
    if i%5 == 0:
        cnt5 +=1

print("3의 배수 : ", cnt3)
print("5의 배수 : ", cnt5)