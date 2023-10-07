import numpy as np   #numpy.ndarray : numpy 라이브러리 안의 배열 ndarray
import matplotlib.pyplot as plt   #약칭으로 plt

# linspace(시작, 끝, 만들 값의 수)
x = np.linspace(0, 14, 50)
# print(type(x), x)
# print(dir(x))
# print(len( dir(x)) )

y1 = np.sin(x)
plt.plot(x, y1, '^')
plt.show()

y2 = np.cos(x)
plt.plot(x, y2, 'o')
plt.show()

y3 = np.tan(x)
plt.plot(x, y3, '-')
plt.show()

# plt.show(x,y1, x,y2, x,y3)