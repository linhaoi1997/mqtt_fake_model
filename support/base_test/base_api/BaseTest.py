from support.tools import go_allure
from support.base_test.base_api.AssertMethod import AssertMethod
import ssl
import pytest
import os


class BaseTestCase(AssertMethod):
    pass


# 运行 pytest 入口
def run(file_name, maxfail=None):
    pro_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    xml_path = pro_dir + "/output/report/xml/"
    if not maxfail:
        pytest.main(['-q', file_name, '--alluredir', xml_path])
    else:
        pytest.main(['-q', file_name, '-x', '--alluredir', xml_path])
    go_allure()


# 工具函数
def collection():
    ssl._create_default_https_context = ssl._create_unverified_context


if __name__ == "__main__":
    test = BaseTestCase()
    test.assertEqual(None, 100)
