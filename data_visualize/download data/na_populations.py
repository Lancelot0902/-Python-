import pygal


wm = pygal.maps.world.World()
wm.title = 'Populations of Countries in North America'

""" 根据人口数量自动绘制深浅不一的颜色 """
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
wm.render_to_file('na_population.svg')