# readlines() 함수를 이용해서 여러줄 출력해 보기
# file = open("hello.txt", encoding = 'utf-8')
# s = file.readline()
# print(s, end='')
# s = file.readline()
# print(s, end='')
# file.close()

#readlines() 함수를 이용해서 단어 검색 몇개인지?
file = open("hello.txt", encoding = 'utf-8')
lines = file.readlines()
for i in lines:
    print(i, end='')
# print(lines)
file.close()