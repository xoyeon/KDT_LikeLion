import random
all_str = ""  # 패스워드 문자열
for x in range(65,122):   #대문자만 91, 소문자는 122 (아스키코드)
    if (x < 91) or (x > 96):  #특수문자 제거
        all_str += chr(x)  # 암호만들 대상 문자열
print(all_str)
print(len(all_str))

def passGen():
    password = ""
    # 10글자 암호
    for i in range(10):
        idx = random.randrange(len(all_str))
        # print(idx)
        password = password + all_str[idx]
    return password
word = passGen()
print("내가 만든 암호 생성기의 암호는 : ", word)