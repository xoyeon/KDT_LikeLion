

# 계산기 클래스 만들기
class Cal:
    result = 0
    def plus(self, num):
        self.result += num
        return self.result
c1 = Cal()
c2 = Cal()
c3 = Cal()
c4 = Cal()
c5 = Cal()
print( c1.plus(8) )
print( c1.plus(5) )
# print( c2.plus(3) )
# print( c2.plus(1) )