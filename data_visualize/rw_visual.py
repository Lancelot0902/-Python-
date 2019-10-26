import matplotlib.pyplot as plt
from random_walk import RandomWalk

""" 模拟多次漫步 """
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    """ 指定图标的宽度、高度 """
    plt.figure(figsize=(10, 6))
    point_number = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_number,
                cmap=plt.cm.Blues, edgecolors='none', s=1)
    """ 突出起点和终点 """
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1],
                c='red', edgecolors='none', s=100)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    """ 设置窗口大小 """
    plt.show()

    keep_running = input("Make another walk(y/n):")
    if keep_running == 'n':
        break
