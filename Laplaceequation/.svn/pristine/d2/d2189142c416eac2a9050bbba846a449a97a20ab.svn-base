import math
import numpy as np
import matplotlib.pyplot as plt


# n1 = int(input("请输入翼型表面离散点数"))
# n2 = int(input("请输入近场到远场离散点数"))
#NACA0012表面坐标
#y1 = 0.6 * (-0.1015 * x**4 + 0.2843 * x**3 - 0.3576 * x**2 - 0.1221 * x + 0.2969 * x ** 0.5)
#y2 = -0.6 * (-0.1015 * x**4 + 0.2843 * x**3 - 0.3576 * x**2 - 0.1221 * x + 0.2969 * x ** 0.5)

#沿x轴等间距变化翼型表面,这样不好
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

#print(math.cos(60/57.3))  #测试python中使用的是弧度制

n1 = 5  #绕翼型一周的点数
n2 = 5  #从壁面到远场的离散点数

#这里用linspace
Theta = np.linspace(0,2*math.pi,num = n1)
X0 = np.ones(n1)
Y0 = np.ones(n1)
X1 = np.ones(n1)
Y1 = np.ones(n1)
X = np.ones([n1,n2])    #存放所有点的横坐标
Y = np.ones([n1,n2])

#-----------------------生成初始网格-------------------#
for i in range(0,n1):
    X0[i] = 0.5 * (1 + math.cos(Theta[i]))
    if(Theta[i]<math.pi):
        y = 0.6 * (-0.1015 * X0[i]**4 + 0.2843 * X0[i]**3 - 0.3576 * X0[i]**2 - 0.1221 * X0[i] + 0.2969 * X0[i] ** 0.5)
    else:
        y = -0.6 * (-0.1015 * X0[i]**4 + 0.2843 * X0[i]**3 - 0.3576 * X0[i]**2 - 0.1221 * X0[i] + 0.2969 * X0[i] ** 0.5)
    Y0[i] = y
    X1[i] = 30 * math.cos(Theta[i]) + 0.5
    Y1[i] = 30 * math.sin(Theta[i])
    #print(X0[i],Y0[i])
    for j in range(0,n2):
        dx = (X1[i] - X0[i]) / (n2 - 1)
        dy = (Y1[i] - Y0[i]) / (n2 - 1)
        X[i][j] = X0[i] + j * dx
        Y[i][j] = Y0[i] + j * dy

#print(X[1][4],Y[1][4])

for i in range(0,n1):
    plt.plot(X[i,:],Y[i,:],'-o',c='b')
    
for j in range(0,n2):
    plt.plot(X[:,j],Y[:,j],'-o',c='b')


plt.axis('square') #等比例显示
plt.show()         #放在最外面，最后只画一张图



#-----------------------生成初始网格-------------------#


'''
# 共用一个show()即可
plt.plot(X0,Y0,'-o')
plt.plot(X1,Y1,'-o')
plt.axis('square')
plt.show()



#迭代解Laplace方程生成网格
dcy = 1     #求解域的横坐标离散
dyt = 1     #求解域的纵坐标离散

#迭代方程中的三个系数，分别为一阶导数关系
alpha = 000
beta  = 000
gama  = 000


X[i][j] = 

Y[i][j] = 



#收敛判据


'''



