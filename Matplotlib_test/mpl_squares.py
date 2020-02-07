import matplotlib.pyplot as plt

input_value=[1,2,3,4,5]
squares=[1,4,9,16,25]
#第一个1对应坐标x=0,input指定了坐标
plt.plot(squares,input_value,linewidth=5)
#设置图标标题，坐标轴加标签
plt.title("Square Number",fontsize=24)
#坐标轴标题
plt.xlabel("value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
#设置刻度标记大小
plt.tick_params(axis='both',labelsize=14)
plt.show()



