# -*- coding: utf-8 -*-
"""
封装层（框架雏形）
把"怎么发请求"和"怎么断言"集中在这里，
用例只关心"测什么"，不关心"怎么发、怎么判"。
"""

import requests

# 1. 配置集中管理：以后换环境只改这一行
BASE_URL = "https://httpbin.org"


# 2. 统一请求方法
def api_get(path, **kwargs):
    """统一的 GET 请求"""
    return requests.get(f"{BASE_URL}{path}", **kwargs)


def api_post(path, **kwargs):
    """统一的 POST 请求"""
    return requests.post(f"{BASE_URL}{path}", **kwargs)


# 3. 统一断言：失败时给出更清楚的报错信息
def assert_status(resp, code=200):
    assert resp.status_code == code, f"期望状态码 {code}，实际 {resp.status_code}"
