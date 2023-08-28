id1 = "toto"
pwd = "1234"
for i in range(1,6):
    yid = input("아이디 입력 : ")
    ypwd = input("비밀번호 입력 : ")
    if id1 == yid:
        if pwd == ypwd:
            print(":: 로그인 성공 ::")
        else:
            print(":: 비밀번호 틀렸습니다. ::")
    else:
        print(":: 아이디가 틀렸습니다 ::")

log_database = {"toto":"1234","one":"3456","two":"0000"}
id1 = input("아이디를 입력하세요: ")
pwd = input("비밀번호를 입력하세요: ")
for i,j in log_database.items():
    if i == id1 and j == pwd:
        print("로그인 성공")
        break
    else:
        print("로그인 실패")
        break