# import matplotlib.pyplot as plt 

# x_values=[1,2,3,4,5]
# y_values=[1,4,9,16,25]

# plt.scatter(x_values,y_values,s=200)
# #调用了scatter()函数，并且用s设置了绘制图形使用点的尺寸

# #设置图表标题，并给坐标轴加上标签
# plt.title("Square Numbers",fontsize=24)
# plt.xlabel("Value",fontsize=14)
# plt.ylabel("Square of Value",fontsize=14)

# #设置刻度标记大小
# plt.tick_params(axis='both',which='major',labelsize=14)

# plt.show()


import matplotlib.pyplot as plt

x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]

#将参数c设置成了一个y值列表，cmap告诉pyplot使用那个颜色映射。
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=40)

#设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])

plt.show()
#要让程序自动保存到文件中，可以将ply.show()替换为plt.savefig()
#第一个实参之定义什么样子的文件保存图表，将存储到scatter_squares.py所在的目录中
#第二个实参将指定图表中多余的空白区域裁剪掉，如果要保留这个空白区域可以省略掉
# plt.savefig('squares_plot1.png',bbox_inches='tight')