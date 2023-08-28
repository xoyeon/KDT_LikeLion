# os 폴더 생성, 폴더에 파일 확인, 폴더 위치 확인.....
import os
import matplotlib.pyplot as plt
import seaborn

# 현재 작업 위치를 알고 싶다.
print( os.getcwd() )  # 현재 작업 폴더를 표시
loc = os.getcwd()

# listdir() 함수는 해당 위치의 파일 및 폴더를 보여준다.
file_list = os.listdir(loc)
print( file_list )