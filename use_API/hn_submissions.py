import requests
from operator import itemgetter
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS


# 执行 API 调用并响应存储
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code: ", r.status_code)

# 处理有关每篇文章的信息
submission_ids = r.json()
title = []
submission_dicts = []
for submission_id in submission_ids[:10]:
    # 对于每篇文章,都执行一个 API 调用
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
        str(submission_id) + '.json')
    submission_r = requests.get(url)
    print("Status code: ", submission_r.status_code)
    response_dict = submission_r.json()
    title.append(response_dict['title'])

    # 根据Value的值绘图
    submission_dict = {
        'value': response_dict.get('descendants', 0),
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id)
    }

    submission_dicts.append(submission_dict)
# 根据comments降序排序
submission_dicts = sorted(submission_dicts,key=itemgetter('value'),reverse=True) 

# 可视化
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most Comments on HackerNews'
chart.x_labels = title

chart.add('comments',submission_dicts)
chart.render_to_file('hacker_news.svg')