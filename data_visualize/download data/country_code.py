from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """ 手动添加未识别出来的国家的国别码 """
    if country_name == 'Yemen,Rep.':
            return 'ye'
    """ 根据指定国家返回两个字母的国别码 """
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code
    return None