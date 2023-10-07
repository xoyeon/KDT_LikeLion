class Cal:
    result = 0
    def plus(self, num):
        self.result += num
        return self.result
    def minus(self, num):
        self.result -= num
        return self.result
    def divide(self, num):
        self.result /= num
        return self.result
# 인스턴스 (객체를 생성)   객체 : 어떤 정보와 행동을 가지고 있다.
c1 = Cal()
c2 = Cal()
c3 = Cal()
c4 = Cal()
c5 = Cal()