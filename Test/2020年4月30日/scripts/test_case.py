import pytest
import os
import allure
import time
import subprocess


@pytest.mark.parametrize('item', ['111', '222'])
def test_case(item):
    allure.dynamic.title(item['case_num'])
    assert 1


def teardown_module():
    time.sleep(5)

    print('1111111111111111111')
    # os.system('allure generate report/result -o report/allure_html --clean')
    subprocess.call("allure generate report/result -o report/allure_html --clean", shell=True)

# if __name__ == '__main__':
#     pytest.main(['test_case.py'])

# def test_case_02():
#     assert 1
#
# def test_case_03():
#     time.sleep(1)
#     assert 1
#
# def teardown_module():
#     os.system('allure generate report/result -o report/allure_html --clean')
