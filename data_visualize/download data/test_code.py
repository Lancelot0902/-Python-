import unittest
from country_code import get_country_code


class TestCountryCode(unittest.TestCase):
    """ 针对country_code模块的测试 """
    def test_country_code(self):
        country_name = 'Yemen,Rep.'
        country_code = 'ye'
        code = get_country_code(country_name)
        self.assertEqual(code,country_code)

unittest.main()