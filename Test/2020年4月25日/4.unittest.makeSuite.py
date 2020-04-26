

import unittest

class Mycase(unittest.TestCase):
    def test_is_upper(self):
        self.assertTrue('Foo'.isupper())

    def test_is_lower(self):
        self.assertTrue('foo'.islower())

    def foo_is_instance(self):
        self.assertTrue([1,2,3],list)


if __name__ == '__main__':
    suite = unittest.makeSuite(testCaseClass=Mycase, prefix='test')
    suite.addTest(Mycase('foo_is_instance'))
    # 执行器执行
    unittest.TextTestRunner().run(suite)