import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 14, 50)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)


plt.figure(figsize=(8,6))
plt.plot(x, y1, '^', label="sin(x)")
plt.plot(x, y2, '--', label="cos(x)")
plt.plot(x, y3, color = 'r', label="tan(x)")
plt.legend()
plt.title("plot")
plt.show()