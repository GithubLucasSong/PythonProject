

# -------------------------addTests---------------------
import unittest

class Mycase(unittest.TestCase):
    def test_is_upper(self):
        self.assertTrue('Foo'.isupper())

    def test_is_lower(self):
        self.assertTrue('foo'.islower())


if __name__ == '__main__':
    case_01 = Mycase(methodName='test_is_upper')
    case_02 = Mycase(methodName='test_is_lower')
    # 创建suite
    suite = unittest.TestSuite()
    # 将用例添加到盒子中
    suite.addTest(case_01)
    suite.addTest(case_02)
    # 使用执行器执行suite中的测试用例
    runner = unittest.TextTestRunner()
    runner.run(suite)


