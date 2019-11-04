import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['system-desgin-primer', 'awesome-python', 'public-apis']

plot_dicts = [
    {'value': 75824, 'label': 'Description of system-desgin-primer.'},
    {'value': 75111, 'label': 'Description of awesome-python.'},
    {'value': 64396, 'label': 'Description of public-apis.'},
    ]
chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')
