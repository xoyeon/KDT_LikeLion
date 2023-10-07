# split() 함수는 문자열에서 해당 구분
# 문자를 이용하여 리스트 형태로 값을 반환해 준다.
line = "Bad, news, travels, fase."
word_list = line.split(":")
print(word_list)

# 3-1 실습 ","구분으로 구분시켜 보기
line = "Bad, news, travels, fase."
word_list = line.split(",")
print(word_list)

for one in word_list:
    print(one)