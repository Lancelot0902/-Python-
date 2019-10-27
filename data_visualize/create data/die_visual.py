import pygal
import matplotlib.pyplot as plt
from die import Die

def toStr(x):
    return str(x)


""" 创建2个D6 """
die_1 = Die()
die_2 = Die(10)

""" 掷几次骰子,并将结果存储在result中 """
results = []
for roll_num in range(5000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

times = []
max_result = die_1.num_sides + die_2.num_sides
for val in range(2,max_result + 1):
    time = results.count(val)
    times.append(time)

""" 对结果进行可视化 """
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times "
hist.x_labels = list(map(toStr,list(range(2,max_result+1))))
hist._x_title = "Results"
hist._y_title = "Frequency of Result"

hist.add('D6 + D10',times)

""" 渲染成svg文件 """
hist.render_to_file('die_visual.svg')
plt.savefig('die_visual.png')