import matplotlib.pyplot as plt

""" 提供输入序列，plot无需对输出值的生成方式作出假设 """
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

""" 设置图标标题 并给坐标轴加上标签 """
plt.title("Squares Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

""" 设置刻度标记大小 """
plt.tick_params(axis='both', labelsize=14)
plt.show()
