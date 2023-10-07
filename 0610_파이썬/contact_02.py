class Contact:
    # 주소록이 만들어질 때, 실행해 주는 생성자
    def __init__(self, name, phone_number, email, addr):
        print("__init__() 함수 시작")
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.addr = addr
    # 주소 정보를 출력해 주는 기능
    def print_info(self):
        print("print_info() 함수 시작")
        print("이름 : ", self.name)
        print("전화번호 : ", self.phone_number)
        print("이메일 : ", self.email)
        print("주소 : ", self.addr)
## 실습4.
## 메뉴만들기 ('1. 연락처 입력, 2: 연락처 출력, 3: 연락처 삭제, 4. 종료')
## 메뉴선택 입력 받아서 넘겨주기
def print_menu():
    print("print_menu() 함수 시작")
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    # 사용자 입력 받은 후, 넘겨주기
    sel_num = int( input("메뉴 선택(1~4) :") )
    return sel_num
def set_contact():
    print("set_contact() 함수 시작")
    name = input("이름 : ")
    phone_number = input("전화번호 : ")
    email = input("이메일(email) : ")
    addr = input("주소(addr) : ")
    return name, phone_number, email, addr
def delete_contact():
    pass

# 여러개의 리스트 출력
def print_contact(c_list):
    for one in c_list:       #  리스트를 하나 하나 불러와서 하나씩 출력해 준다.
        one.print_info()
    # --.print_info()
def run():
    print("run() 함수 시작")
    menu = 0

    contact_all = []  # ----

    while (menu!=4):
        menu = print_menu()
        if menu==4:
            print("프로그램을 종료합니다.")
        elif menu==1:
            a1, a2, a3, a4 = set_contact()  # 연락처 사용자 입력
            one = Contact(a1, a2, a3, a4)     # 연락처 클래스 객체 만들기
            contact_all.append(one)   # ----
        elif menu==2:
            try:
                # print_contact( ____ )
                # k.print_info()
            except UnboundLocalError as e:
                print("데이터 없음.", e)
        elif menu==3:
            try:
                del k
            except:
                print("데이터 없음.", e)
        # elif ______:  # men1u 출력일 때
        #    출력 부분(k)
    # a1, a2, a3, a4 = set_contact()
    # k = Contact("kim",
    #             '010-222-3333',
    #             'fron1020@naver.com',
    #             '경기도 분당')
    #k = Contact(a1, a2, a3, a4)
    #k.print_info()
if __name__=="__main__":
    run()
## 실습1.
## 이름, 전화번호, 이메일, 주소
## 생성자에 추가, 출력 기능에 추가해주기
## 실습2. 실제로 입력해서 실행하는 함수. 그리고 if __name__=="__main__"
## 실습3. 직접 입력하는 기능을 넣어보자.
## 실습4.
## 메뉴만들기 ('1. 연락처 입력, 2: 연락처 출력, 3: 연락처 삭제, 4. 종료')
## 메뉴선택 입력 받아서 넘겨주기
## 실습5
## 1,2,3 선택 후, 실행 된 이후에 다시 원래 메뉴를 띄워주어야 한다.(while)
## 4번(종료)가 입력되면 프로그램 종료.
## 실습 6
## 1번 일때는 연락처 입력 동작
## 2번 일때는 연락처 출력 동작
## 실습 7
## 3번을 선택하면 연락처를 삭제하기
## 실습 8
## 여러 개의 추가하고 싶다.
## 실습 9
## 주소록의 데이터를 여러 개의 출력하고 싶다.