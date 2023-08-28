# open() 파일 열때
# read()      : 파일의 전체 문자열 가져오기
# readline()  : 문자열을 한줄식 가져오기
# readlines() : 문자열을 줄단위로 리스트를 가져오기

# open("파일명", 'r')  ; 읽기모드
# open("파일명", 'w')  ; 파일 생성 모드
# open("파일명", 'a')  ; 파일 생성 및 파일 추가 모드


# var = open("hello22.txt", "r", encoding = 'utf-8') ## 읽기만 할거야.
# print( var.read() )
# var.close()


# f1 = open("hello55.txt", "w") ## 생성 후 덮어쓰기
# f1.write("monitor, 20000")
# f1.close()


f1 = open("hello55.txt", "a") ## 추가하기
f1.write("monitor, 20000")
f1.close()