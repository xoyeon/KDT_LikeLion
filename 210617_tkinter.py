from tkinter import *
import pandas as pd
import os    # 폴더를 만들고, 삭제 ... 현재 폴더 위치.

print(os.getcwd())    # cwd : current working directory; 현재 작업 위치 확인

# 파일 불러오기
# dat = pd.read_excel("./dic_excel.xlsx")    # 해당폴더 : . / 상위폴더 : ..
dat = pd.read_csv("./한국전력공사.csv", encoding = 'euc-kr')   #  iconv -f cp949 -t utf-8 원본.csv > 새로운.csv
print(dat.columns)


# 기능 추가
# 제출 버튼을 클릭했을 때, 동작 기능.
def click():
    print("버튼이 클릭되었습니다.")
    # pass
    word = entry.get()  # 아래 엔트리 상자의 내용을 text로 넣는다.

    # END로 지정하면 문자열이 입력된 최종 입력 지점을 의미.
    # 특정 시작 지점부터 텍스트 엔트리 위젯의 끝까지 모두 지우기 위해 END를 쓴다.
    output.delete(0.0, END)  # 텍스트 박스 내용을 지운다.

    try:
        # def_word = dat.loc[dat['word'] == word, 'def'].values[0]
        # csv 파일 목록에 "순번, 용어, 용어설명"으로 나와있기 때문에 다음과 같이 사용 --
        def_word = dat.loc[dat['용어'] == word, '용어설명'].values[0]
    except:
        def_word = "단어를 뜻을 찾을 수 없음."
    output.insert(END, def_word)


window = Tk()
window.title("My Dictionary")

# 01 입력 상자 설명 레이블
label = Label(window, text="원하는 단어 입력 후, 엔터 키 누르기")
label.grid(row=0, column=0, sticky=W)   # W는 west, 방향표시

# 02 텍스트 입력이 가능한 상자(Entry)
entry = Entry(window, width=15, bg="light green")
entry.grid(row=1, column=0, sticky=W)

# 03 제출 추가해 보기(Exit)
button = Button(window, text="제출", width=5, command = click)
button.grid(row=2, column=0, sticky=W)

# 04 설명 레이블 - 의미
label2 = Label(window, text="\n의미 : ")
label2.grid(row=3, column=0, sticky=W)

# 05 텍스트 박스 입력 상자
# columnspan=2 는 (4,0)~(4,1) 위치까지 분포
output = Text(window, width=50, height=6, wrap=WORD, background="light green")  # wrap : 줄바꿈
output.grid(row=4, column=0, columnspan=2, sticky=W)

# 메인 반복문 실행
window.mainloop()