# fruits = ['사과', '과일', '포도']
# print(fruits[1])

# try:
#     fruits = ['사과', '과일', '포도']
#     print(fruits[4])
# except IndexError:
#     print("인덱스 에러가 발생 : ", IndexError)
# except NameError:
#     print("변수가 정의되지 않았습니다", IndexError)
# except Exception as e:
#     print("변수가 정의되지 않았습니다", IndexError)

try:
    fruits = ['사과', '과일', '포도']
    print(fruits[4])
except IndexError:
    print("인덱스 에러가 발생 : ", IndexError)
except SyntaxError:
    print("문법적인 오류가 발생했습니다. : ", SyntaxError)