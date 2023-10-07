import matplotlib.pyplot as plt
import matplotlib

print(matplotlib.__version__)
plt.plot([1,2,3], [10,20,30], 'o')
plt.show()
#######################################3
import matplotlib.pyplot as plt
import matplotlib

x = [1,2,3,4,5]
y = [10,20,30,40,50]
# plt.plot(x, y, marker='^', color='r')
# plt.plot(x, y, marker='^', color='r')
plt.plot(x, y, 'r^')
plt.title("title")
plt.show()