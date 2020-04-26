

import unittest


class Mycase(unittest.TestCase):
    def test_is_upper(self):
        self.assertTrue('Foo'.isupper())

    def test_is_lower(self):
        self.assertTrue('foo'.islower())


if __name__ == '__main__':
    suite = unittest.makeSuite(testCaseClass=Mycase,prefix='test')
    # 执行器执行
    unittest.TextTestRunner().run(suite)
