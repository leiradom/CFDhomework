import math
import numpy as np
import matplotlib.pyplot as plt

#数组准备
X = np.ones(100)
Y1 = np.ones(100)
Y2 = np.ones(100)


# n1 = int(input("请输入翼型表面离散点数"))
# n2 = int(input("请输入近场到远场离散点数"))

#NACA0012表面坐标
#y1 = 0.6 * (-0.1015 * x**4 + 0.2843 * x**3 - 0.3576 * x**2 - 0.1221 * x + 0.2969 * x ** 0.5)
#y2 = -0.6 * (-0.1015 * x**4 + 0.2843 * x**3 - 0.3576 * x**2 - 0.1221 * x + 0.2969 * x ** 0.5)

for i in range (0,100):
    x = 0.01 *  i
    y1 = 0.6 * (-0.1015 * x**4 + 0.2843 * x**3 - 0.3576 * x**2 - 0.1221 * x + 0.2969 * x ** 0.5)
    y2 = -0.6 * (-0.1015 * x**4 + 0.2843 * x**3 - 0.3576 * x**2 - 0.1221 * x + 0.2969 * x ** 0.5)
    X[i] = x
    Y1[i] = y1
    Y2[i] = y2
plt.plot(X,Y)
plt.show()
