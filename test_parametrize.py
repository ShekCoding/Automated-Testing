# -*- coding: utf-8 -*-
"""
第二课：参数化 @pytest.mark.parametrize
运行：pytest test_parametrize.py -v
"""

import requests
import pytest

BASE = "https://httpbin.org"


# 例子1：一个函数，测 6 种状态码
@pytest.mark.parametrize("code", [200, 201, 204, 400, 404, 500])
def test_status_codes(code):
    """对每个 code，都请求一次并断言返回对应状态码"""
    r = requests.get(f"{BASE}/status/{code}")
    assert r.status_code == code


# 例子2：数据驱动——同一逻辑，跑多组参数
@pytest.mark.parametrize(
    "name,age",
    [
        ("shi", 28),
        ("zhang", 30),
        ("li", 25),
    ],
)
def test_get_with_params(name, age):
    """服务端应该原样收到我发的 name 和 age"""
    r = requests.get(f"{BASE}/get", params={"name": name, "age": age})
    assert r.status_code == 200
    assert r.json()["args"]["name"] == name
    assert r.json()["args"]["age"] == str(age)
