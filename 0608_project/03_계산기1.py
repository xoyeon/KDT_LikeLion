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
# 01 색깔을 넣어주세요.
# 02 초기 메시지 넣기.
# 03 곱하기 기능 추가
# 04 나누기 기능 추가
class Adv_Cal(Cal):
    color = 'blue'    # color 색깔정보
    # 초기메시지
    print('SamSung')
    print(color)
    print('업그레이드 된 버전입니다!')
    def divide(self, num):
        if num == 0:
            return '0으로 나눌 수 없어요.'
        else:
            self.result /= num
            return self.result
    def multiple(self, num):
        self.result *= num
        return self.result
# 새로운 계산기 2대 생산
c1 = Adv_Cal()
c2 = Adv_Cal()
# 첫번째 계산기 테스트
print()
print('< c1 >')
print(c1.plus(6))
print(c1.divide(0))
print(c1.divide(2))
print(c1.multiple(3))
# 두번째 계산기 테스트
print()
print('< c2 >')
print(c2.minus(3))
print(c2.multiple(4))
print(c2.divide(-2))