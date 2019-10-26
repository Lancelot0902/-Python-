import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = r'F:\Python\program\data_visualize\death_valley_2014.csv'
with open(filename) as f:
    """ 得到一个与文件关联的阅读器 """
    reader = csv.reader(f)

    """ 返回文件中的下一行 """
    header_row = next(reader)

    """ 返回head_row中每个元素的索引和值 """
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates, highs, lows = [], [], []
    """ next读取完当前行后会自动返回下一行 """
    """ 从文件中获取日期,最高气温,最低气温 """
    for row in reader:
        try:
            """ 转换成日期对象 """
            date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(date, "Missing data")
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

    fig = plt.figure(dpi=128, figsize=(10, 6))

    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    """ 设置图形格式 """
    plt.title("Daily high and low temperatures,July 2014", fontsize=24)
    plt.xlabel("", fontsize=16)

    """ 绘制斜的日期标签以免重叠 """
    fig.autofmt_xdate()
    plt.ylabel("Temperature(F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
