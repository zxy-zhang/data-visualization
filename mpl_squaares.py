import matplotlib.pyplot as plt 
#导入模块pyplot，指定别名plt
input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]
plt.plot(input_values,squares,linewidth=5)
#这个函数尝试根据这些数据绘制有意义的图形

#设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis="both",labelsize=14)

#这个函数尝试根据这些数据绘制有意义的图形
plt.show()
#打开matplotlib查看器，并且查看绘制的图形