import matplotlib.pyplot as plt
from Matplotlib_test.RandomWalk import RandomWalk1

#创建实例
# rw=RandomWalk1()
#如果想增大数据
rw=RandomWalk1(5000)
rw.fill_walk()
#绘制窗口,单位英寸，dpi是分辨率
plt.figure(figsize=(10,6))

#突出起点终点
plt.scatter(0,0,c='green',edgecolors='none',s=100)
plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=0.1)
#隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.scatter(rw.x_values,rw.y_values,s=15)
plt.show()