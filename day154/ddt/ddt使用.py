import unittest
import ddt
import requests
from HTMLTestRunner import HTMLTestRunner

data_list = [
    {"url": "https://cnodejs.org/api/v1/topics", "method": "get"},
    {"url": "https://cnodejs.org/api/v1/topic/5433d5e4e737cbe96dcef312", "method": "get"},
    {"url": "https://cnodejs.org/api/v1/topic_collect/collect", "method": "post"},
    {"url": "https://cnodejs.org/api/v1/topic_collect/de_collect", "method": "post"},
    {"url": "https://cnodejs.org/api/v1/user/alsotang", "method": "get"},
    {"url": "https://cnodejs.org/api/v1/message/mark_all", "method": "post"},
]
@ddt.ddt
class MyCase(unittest.TestCase):
    @ddt.data(*data_list)
    def test_case(self,item):
        # print(11111111,item)
        response = requests.request(
            url=item['url'],
            method=item['method']
        )
        self.assertEqual(response.status_code,200)



if __name__=='__main__':
    suite = unittest.makeSuite(testCaseClass=MyCase,prefix='test')
    with open('report.html', 'wb') as f:
        HTMLTestRunner(
            stream=f,
            title = 'ddt示例报告',
            description='演示ddt和HTMLTestRunner结合用法',
            verbosity=2,
        ).run(suite)