class Contact:
    # 주소록이 만들어질 때, 실행해 주는 생성자
    def __init__(self, name, tel, mail, add):
        self.name = name
        self.tel = tel
        self.mail = mail
        self. add = add
        pass


    # 주소 정보를 출력해 주는 기능
    def print_info(self):
        print("이름 : ", self.name)
        print("전화번호 : ", self.tel)
        print("메일 : ", self.mail)
        print("주소 : ", self.add)
        pass

def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")

    # 사용자 입력 받은 후, 넘겨주기
    sel_num = int(input("메뉴선택(1~4) :"))
    return sel_num

def set_contact():
    name = input("Name : ")
    tel = input("Tele : ")
    mail = input("E-mail : ")
    add = input("Address : ")
    return name, tel, mail, add

def run():
    a1, a2, a3, a4 = set_contact()
    print(type(a1), type(a2), type(a3), type(a4))

    k = Contact(a1, a2, a3, a4)
    k.print_info()

def run_2():
    menu = 0
    while (menu!=4):
        menu = print_menu()
        if menu == 4:
            print("프로그램을 종료합니다.")
        elif menu == 1:
            a1, a2, a3, a4 = set_contact()   # 연락처 입력
            k = Contact(a1, a2, a3, a4)      # 연락처 클래스 객체 만들기
        # elif ___: #menu 출력일 때
        #     #  출력부분(k)

if __name__ == "__main__":
    run_2()

## 실습6 :  1.연락처입력, 2.연락처출력
## 실습7 : 3번을 선택하면 연락처를 삭제하기