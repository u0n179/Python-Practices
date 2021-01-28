import numpy as np
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace
# print(plt.matplotlib_fname()) 
# data=np.arange(0,5,0.01)
# plt.title('画图测试') ## 添加标题
# plt.xlabel('x')## 添加x轴的名称
# plt.ylabel('y')## 添加y轴的名称
# plt.xlim((0,5))## 确定x轴范围
# plt.ylim((0,5))## 确定y轴范围
# plt.xticks([0,5])## 规定x轴刻度
# plt.yticks([0,25])## 确定y轴刻度
# plt.plot(data,data**2)## 添加y=x^2曲线
# plt.plot(data,data**4)## 添加y=x^4曲线
# plt.legend(['y=x^2','y=x^4'])
# plt.savefig('d:/codes/python/y=x^2.png')
# plt.show()

x=linspace(0,np.pi)
y=np.sin(x)
## 无法显示中文标题
# plt.plot(x,y,label="$sin(x)$")## 绘制三角函数
# plt.title('sin曲线')
# plt.savefig('d:/codes/python/无法显示中文标题sin曲线.png')
# plt.show()
##设置rc参数显示中文标题
## 设置字体为SimHei显示中文
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False ## 设置正常显示符号
plt.plot(x,y,label="$sin(x)$")## 绘制三角函数
plt.title('sin曲线')
plt.savefig('d:/codes/python/显示中文标题sin曲线.png')
plt.show()



