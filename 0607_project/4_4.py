id1 = "toto"
pwd = "1234"
num = 0
while num != 5:
    yid = input("아이디 입력 : ")
    ypwd = input("비밀번호 입력 : ")
    if (yid==id1) and (ypwd==pwd) :
        print("로그인 성공")
        break
    elif (yid==id1) :
        print("비밀번호를 확인해주세요.")
    elif (ypwd==pwd):
        print("아이디를 확인해주세요.")
    else :
        num += 1
        print("로그인 %d회 실패하셨습니다."%num)