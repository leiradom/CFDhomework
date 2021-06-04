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



#定义常数
n1 = 29      #绕翼型一周的点数
n2 = 29       #从壁面到远场的离散点数
e1 = 0.1
e2 = 0.1
e0 = 1e-3      #设定收敛残值
dcx = 1     #求解域的横坐标离散
dcy = 1     #求解域的纵坐标离散
a = 0
b = 0
g = 0
#这里用linspace
Theta = np.linspace(0,2*math.pi,num = n1)
X0 = np.ones(n1)
Y0 = np.ones(n1)
X1 = np.ones(n1)
Y1 = np.ones(n1)
X = np.ones([n1,n2])    #存放所有点的横坐标
Y = np.ones([n1,n2])    #c
x2 = np.ones([n1,n2])    #迭代用
y2 = np.ones([n1,n2])    #迭代用

#-----------------------生成网格初值-------------------#
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

'''
#显示初始网格
for i in range(0,n1):
    plt.plot(X[i,:],Y[i,:],'-o',c='b')
    
for j in range(0,n2):
    plt.plot(X[:,j],Y[:,j],'-o',c='b')
plt.axis('square') #等比例显示
plt.show()         #放在最外面，最后只画一张图
'''
#-----------------------生成网格初值-------------------#


#迭代解Laplace方程生成网格


while((e1 > e0) or (e2 > e0)):
    for i in range(0,n1):
        for j in range(1,n2-1):
            if(i == 0):
                a = ((X[i][j+1]-X[i][j-1]) / (2*dcy))**2 + ((Y[i][j+1]-Y[i][j-1]) / (2*dcy))**2   #alpha
                b  = ((X[i+1][j]-X[n1-1][j]) / (2*dcx)) * ((X[i][j+1] - X[i][j-1]) / (2*dcy)) \
                        + ((Y[i+1][j]-Y[n1-1][j]) / (2*dcx))*((Y[i][j+1] - Y[i][j-1]) / (2*dcy))  #beta
                g  = ((X[i+1][j]-X[n1-1][j]) / (2*dcx))**2 + ((Y[i+1][j]-Y[n1-1][j]) / (2*dcx))**2  #gamma
                #开始迭代
                x2[i][j] = 0.5 * (a * (X[i+1][j] + X[n1-1][j]) + g * (X[i][j+1] + X[i][j-1]) \
                - 0.5 * b * (X[i+1][j+1]+X[n1-1][j-1]-X[i+1][j-1]-X[n1-1][j+1])) / (a + g)
                y2[i][j] = 0.5 * (a * (Y[i+1][j] + Y[n1-1][j]) + g * (Y[i][j+1] + Y[i][j-1]) \
                - 0.5 * b * (Y[i+1][j+1]+ Y[n1-1][j-1]- Y[i+1][j-1]- Y[n1-1][j+1])) / (a + g)
                e1 = abs(X[i][j] - x2[i][j])
                e2 = abs(Y[i][j] - y2[i][j])
                X[i][j] = x2[i][j]   #更新迭代的x坐标
                Y[i][j] = y2[i][j]   #更新迭代的y坐标
            #迭代方程中的三个系数，分别为一阶导数关系
            elif(i == n1 - 1):
                X[i][j] = X[0][j]   #更新迭代的x坐标
                Y[i][j] = Y[0][j]   #更新迭代的y坐标
            else:
                a = ((X[i][j+1]-X[i][j-1]) / (2*dcy))**2 + ((Y[i][j+1]-Y[i][j-1]) / (2*dcy))**2   #alpha
                b  = ((X[i+1][j]-X[i-1][j]) / (2*dcx)) * ((X[i][j+1] - X[i][j-1]) / (2*dcy)) \
                        + ((Y[i+1][j]-Y[i-1][j]) / (2*dcx))*((Y[i][j+1] - Y[i][j-1]) / (2*dcy))  #beta
                g  = ((X[i+1][j]-X[i-1][j]) / (2*dcx))**2 + ((Y[i+1][j]-Y[i-1][j]) / (2*dcx))**2  #gamma
                #开始迭代
                x2[i][j] = 0.5 * (a * (X[i+1][j] + X[i-1][j]) + g * (X[i][j+1] + X[i][j-1]) \
                - 0.5 * b * (X[i+1][j+1]+X[i-1][j-1]-X[i+1][j-1]-X[i-1][j+1])) / (a + g)
                y2[i][j] = 0.5 * (a * (Y[i+1][j] + Y[i-1][j]) + g * (Y[i][j+1] + Y[i][j-1]) \
                - 0.5 * b * (Y[i+1][j+1]+ Y[i-1][j-1]- Y[i+1][j-1]- Y[i-1][j+1])) / (a + g)
                e1 = abs(X[i][j] - x2[i][j])
                e2 = abs(Y[i][j] - y2[i][j])
                X[i][j] = x2[i][j]   #更新迭代的x坐标
                Y[i][j] = y2[i][j]   #更新迭代的y坐标

#最终绘图
for i in range(0,n1):
    plt.plot(X[i,:],Y[i,:],c='b')
    
for j in range(0,n2):
    plt.plot(X[:,j],Y[:,j],c='b')
plt.axis('square') #等比例显示
plt.show()         #放在最外面，最后只画一张图