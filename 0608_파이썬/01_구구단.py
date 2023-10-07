for i in range (2, 10, 1):
    print() #줄 간격 삽입
    for j in range(1, 10, 1):
        print("{} * {} = {}".format(i, j, i*j))


# def gugu(a):
#     result=[a*i for i in range(1,11) if a<=9 ]
#     return result
# guk=int(input("원하는 구구단의 단을 입력하세요:"))
# guk2=gugu(guk)
# print(guk2)

# 구구단 프로그램(강사님)
# w_dan = int(input("내가 출력을 원하는 단 :"))
# for i in range(2, 10, 1):
#     if i==w_dan:
#         for j in range(1, 10, 1):
#             print("{} * {} = {}".format(i , j, i*j))
#         print()