# -*- coding: utf-8 -*-
"""
第七课：JSON 断言 / jsonpath
运行：pytest test_jsonpath.py
"""

import requests
from jsonpath import jsonpath

# 模拟一个接口返回的嵌套 JSON
SAMPLE = {
    "code": 200,
    "data": {
        "user": {"name": "shi", "age": 28},
        "orders": [
            {"id": 1, "price": 99.9},
            {"id": 2, "price": 199.9},
        ],
    },
}


def test_jsonpath_field():
    """取普通字段"""
    # $.code          → 取根下的 code
    assert jsonpath(SAMPLE, "$.code") == [200]
    # $.data.user.name → 逐层往下取
    assert jsonpath(SAMPLE, "$.data.user.name") == ["shi"]


def test_jsonpath_list():
    """取列表里的元素"""
    # [0] 取第一个元素
    assert jsonpath(SAMPLE, "$.data.orders[0].id") == [1]
    # [*] 取所有元素的某个字段
    assert jsonpath(SAMPLE, "$.data.orders[*].price") == [99.9, 199.9]


def test_jsonpath_real_api():
    """用 jsonpath 断言真实接口返回"""
    r = requests.get("https://httpbin.org/get", params={"name": "shi"})
    assert r.status_code == 200
    # 从真实响应里取嵌套字段
    assert jsonpath(r.json(), "$.args.name") == ["shi"]
