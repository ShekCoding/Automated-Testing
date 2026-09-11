# -*- coding: utf-8 -*-
"""
conftest.py：pytest 会自动读取这个文件
放共享的 fixture、自定义命令行参数等
"""
import pytest
from common.config import ENVIRONMENTS


# 自定义命令行参数 --env，默认 test
def pytest_addoption(parser):
    parser.addoption("--env", default="test", help="选择环境：test / staging / prod")


# session 级 fixture：根据 --env 返回对应环境的基础地址
@pytest.fixture(scope="session")
def base_url(request):
    env = request.config.getoption("--env")
    return ENVIRONMENTS[env]
