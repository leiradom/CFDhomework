import math
import numpy as np
import matplotlib.pyplot as plt

#数组准备
X = np.ones(101)
Y1 = np.ones(101)
Y2 = np.ones(101)


# n1 = int(input("请输入翼型表面离散点数"))
# n2 = int(input("请输入近场到远场离散点数"))

#NACA0012表面坐标
#y1 = 0.6 * (-0.1015 * x**4 + 0.2843 * x**3 - 0.3576 * x**2 - 0.1221 * x + 0.2969 * x ** 0.5)
#y2 = -0.6 * (-0.1015 * x**4 + 0.2843 * x**3 - 0.3576 * x**2 - 0.1221 * x + 0.2969 * x ** 0.5)


#沿x轴等间距变化翼型表面
'''
for i in range (0,101):
    x = 0.01 *  i
    y1 = 0.6 * (-0.1015 * x**4 + 0.2843 * x**3 - 0.3576 * x**2 - 0.1221 * x + 0.2969 * x ** 0.5)
    y2 = -0.6 * (-0.1015 * x**4 + 0.2843 * x**3 - 0.3576 * x**2 - 0.1221 * x + 0.2969 * x ** 0.5)
    X[i] = x
    Y1[i] = y1
    Y2[i] = y2
plt.plot(X,Y1,'-o')
plt.plot(X,Y2,'-o')
plt.show()
'''

print(math.cos(60/57.3))

R = 30

#这里用linspace
Theta = np.linspace(0,2*math.pi,num = 50)
X = 0.5 * (1 + np.cos(Theta))
Y = np.ones(50)
for i in range(0,50):
    if(Theta[i]<math.pi):
        y = 0.6 * (-0.1015 * X[i]**4 + 0.2843 * X[i]**3 - 0.3576 * X[i]**2 - 0.1221 * X[i] + 0.2969 * X[i] ** 0.5)
    else:
        y = -0.6 * (-0.1015 * X[i]**4 + 0.2843 * X[i]**3 - 0.3576 * X[i]**2 - 0.1221 * X[i] + 0.2969 * X[i] ** 0.5)
    Y[i] = y
    print(X[i],Y[i])

plt.plot(X,Y,'-o')
plt.show()





