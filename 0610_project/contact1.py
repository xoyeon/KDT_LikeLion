# 01. class와 함수 정의
class Contact:
    def __init__(self, name, phone_number, email, addr):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.addr = addr

    #  출력 기능
    def print_info(self):
        print("이름 : ", self.name)
        print("전화번호 : ", self.phone_number)
        print("이메일 : ", self.email)
        print("주소 : ", self.addr)

## 여러개의 연락처를 출력하는 함수 만들기
def print_contact(c_list):
    for one in c_list: # ___   #  리스트를 하나 하나 불러와서 하나씩 출력해 준다.
        one.print_info()

## 하나의 연락처를 삭제하는 함수 만들기
def delete_contact(d_name, c_list):
    idx = 0
    for one in c_list:
        if d_name == one.name :
            print(f"{d_name}의 연락처가 삭제되었습니다.")
            del c_list[idx]
        idx += 1

def print_menu():
    print("print_menu() 함수 시작")
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")

    # 사용자 입력 받은 후, 넘겨주기
    sel_num = int( input("메뉴 선택(1~4) :") )
    return sel_num
# 사용자에게 정보를 입력받고 연락처 하나 생성.
def set_contact():
    name = input("이름 : ")

    while len(name) > 30 :
        print("이름이 30자가 넘어갑니다. 다시 입력 부탁드려요.")
        name = input("이름 : ")


    phone_number = input("전화번호 : ")
    email = input("이메일(email) : ")
    addr = input("주소(addr) : ")
    one = Contact(name, phone_number, email, addr)
    return one

def run():

    # 입력, 출력, 삭제, 종료

    c_all = []
    menu_sel = 0
    while menu_sel != 4:
        menu_sel = print_menu()
        print("메뉴 선택 : ", menu_sel)
        if menu_sel == 1:
            one1 = set_contact()
            c_all.append(one1)
        elif menu_sel == 2:
            print_contact(c_all)
        elif menu_sel == 3:
            name1 = input("삭제할 연락처 이름은 : ")
            delete_contact(name1, c_all)


    one1.print_info()
    # one = Contact("kim", "010-0000-1111", "ddd@naver.com", '경기도 분당')
    # one.print_info()

if __name__ == "__main__":     # 파이썬에서 직접 실행시킬 때
    run()