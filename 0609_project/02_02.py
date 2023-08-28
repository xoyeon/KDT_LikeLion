# class Cal:
#     pass

# a = Cal()
# b = Cal()

# 첫번째 계산기
result1 = 0
def plus1(num):
    global result1
    result1 += num
    return result1
print(plus1(3))
print(plus1(4))

# 두번째 계산기
result2 = 0
def plus2(num):
    global result2
    result2 += num
    return result2
print(plus2(3))
print(plus2(4))

class Cal:
    result = 0
    def plus(self, num):
        self.result += num
        return self.result
# 나머지 계산기 네대
a1 = Cal()  # 계산기 한대
a2 = Cal()  # 계산기 한대
a3 = Cal()  # 계산기 한대
a4 = Cal()  # 계산기 한대
a5 = Cal()  # 계산기 한대