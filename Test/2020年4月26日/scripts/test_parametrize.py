url_list = [
    {'url': "https://www.baidu.com", "method": "get", "status": 200},
    {'url': "https://www.cnblogs.com/Neeo/articles/11832655.html", "method": "get", "status": 200},
    {'url': "http://www.neeo.cc:6001/post", "method": "post", "status": 200},
    {'url': "http://www.neeo.cc:6001/put", "method": "put", "status": 200},
]

import pytest
import requests


@pytest.mark.parametrize('item', url_list)
def test_case(item):
    print(item['status'])
    response = requests.request(method=item['method'],url=item['url'])
    assert response.status_code == item['status']

