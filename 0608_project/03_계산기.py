# (1) 나누기 기능이 정상적이지 않아요.
# (2) 곱하기 기능 추가해 주세요.
# (3) 색깔도 넣어주세요.
# (4) 초기 메세지 넣기
# 4-1 개량된 계산기 틀(class)만들기


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

class cal_ch:
