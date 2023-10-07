class Contact:
    def __init__(self, name, phone_number, email, addr):
        print("__init__() 함수 시작")
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.addr = addr

    def print_info(self):
        print("print_info() 함수 시작")
        print("이름 : ", self.name)
        print("전화번호 : ", self.phone_number)
        print("이메일 : ", self.email)
        print("주소 : ", self.addr)

def print_menu():
    print("print_menu() 함수 시작")
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")

    sel_num = int( input("메뉴 선택(1~4) :") )
    return sel_num

def set_contact():
    print("set_contact() 함수 시작")
    name = input("이름 : ")
    phone_number = input("전화번호 : ")
    email = input("이메일(email) : ")
    addr = input("주소(addr) : ")
    return name, phone_number, email, addr

def delete_contact(d_name, c_list):
    for idx, one in enumerate(c_list):
        if d_name == one.name:
            print(f"{d_name}의 연락처가 삭제되었습니다.")
            del c_list[idx]

# 여러개의 리스트 출력
def print_contact(c_list):
    for one in c_list: # ___   #  리스트를 하나 하나 불러와서 하나씩 출력해 준다.
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
                print_contact( contact_all )
                # k.print_info()
            except UnboundLocalError as e:
                print("데이터 없음.", e)
        elif menu==3:
            ## 삭제할 이름은 무엇인가요?
            del_name = input("삭제할 연락처 이름은?")
            delete_contact(del_name, contact_all)

if __name__=="__main__":
    run()