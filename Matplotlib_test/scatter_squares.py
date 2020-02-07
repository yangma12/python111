import matplotlib.pyplot as plt
xvalue = list(range(1,1001))
yvalue = [x**2 for x in xvalue]
plt.scatter(xvalue,yvalue,s=20)
#设置图表
plt.title("Square Number",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("S_Value",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize=14)
plt.show()
plt.savefig('squares_plot.png',bbox_inches='tight')#自动保存