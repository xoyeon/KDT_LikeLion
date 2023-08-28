### 파일 읽고 쓰기
### open()

f = open("C:\hello.txt", 'r', encoding = 'utf-8')
print( f.read() )
f.close()

# 지역변수 vs 전역변수 : 전역변수(함수 밖에서 사용가능), 지역변수()
# global
# chr(65) : 유니코드 아스키코드로 변경해 준다.
# import random : 리스트를 갖는 값들중에 임의의 어떤 값 또는 숫자를 선택해 주는 것
# 텍스트 파일
# 이진파일(binary file)
# write(") 파일에 내용 적기