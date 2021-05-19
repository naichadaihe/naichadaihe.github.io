# -*- coding: UTF-8 -*-
#coding=utf-8

import matplotlib.pyplot as plt
import numpy as np 
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
x = np.linspace(0, 3 * np.pi, 100)
y = np.sin(x)

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(1,2,1)#一行两列，第一个图
plt.title(r'$f(x)=sin(x)$') #设置标题
plt.plot(x, y)#以（x，y）为坐标轴显示函数
#plt.show()

x1 = [t*0.375*np.pi for t in x]#x赋值给t，w=t*0.375π
y1 = np.sin(x1)#定义sin函数
plt.subplot(1,2,2)#一行两列，第二个图
# plt.title(u"测试2") #注意：在前面加一个u
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$') #设置标题
plt.plot(x1, y1)#以（x，y）为坐标轴显示函数
plt.show()