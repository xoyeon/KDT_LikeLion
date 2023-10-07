import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 14, 50)
y1 = np.cos(x1)

x2 = np.linspace(0, 14, 50)
y2 = np.sin(x2)

x3 = np.linspace(0, 14, 50)
y3 = np.tan(x3)

plt.plot(x1,y1,'go', x2,y2,'g-', x3,y3,'g^')
plt.show()