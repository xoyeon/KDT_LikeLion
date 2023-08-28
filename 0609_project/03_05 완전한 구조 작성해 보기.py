# try:
#     사물놀이 = ["장구", "북", "징"]
#     print(사물놀이[4])
# except IndexError:           #예외가 발생 시 , 실행 코드
#     print("다시 입력하세요.")
# else:                        #예외가 없을 때 실행 코드
#     print("없는 단어입니다.")
# finally:                     #예외에 상관없이 무조건 실행될 코드
#     print("그냥 합니다.")

def divide(a,b):
    return a/b
try:
    c = divide(5, 2)
except ZeroDivisionError:
    print("두번째 인자가 0이어서는 안된다.")
except TypeError:
    print("[에러] {} {}모든 인자는 숫자여야 합니다.".format(5,'string'))
except Exception as e:
    print("에러 발생 : ", e)
else:
    print("결과 값은 {}".format(c))
finally:
    print("프로그램 실행이 완료되었습니다.")