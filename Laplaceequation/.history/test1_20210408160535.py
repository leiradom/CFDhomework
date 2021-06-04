import math 
import numpy as np

a = np.ones([2,100])
n = 5
#write 数据到 dat 文件里
with open('CQ.dat','w') as f1:
    for i in range(100):
        f1.write(f' wo  {n} \n')     #f执行大括号里面的函数