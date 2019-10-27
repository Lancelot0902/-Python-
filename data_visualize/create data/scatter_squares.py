import matplotlib.pyplot as plt

""" 使用scatter绘制散点图并设置样式 """
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values,
            cmap=plt.cm.Blues, edgecolors='none', s=40)

""" 设置表的标题并给坐标轴加上标签 """
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square Value", fontsize=14)

""" 设置刻度标记 """
plt.tick_params(axis='both', which='major', labelsize=14)

""" 指定每个坐标轴的取值范围 """
plt.axis([0, 1100, 0, 1100000])

""" 自动保存图片 """
plt.savefig('squares_plot.png')
plt.show()
