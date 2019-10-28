import pygal


wm = pygal.maps.world.World()
wm.title = 'North, Central, South America'

""" 接受一个标签和要突出的国别码,每次调用add都会选择一种不同的颜色 """
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co',
                         'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')
