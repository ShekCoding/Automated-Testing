# -*- coding: utf-8 -*-
"""
接口自动化测试第一课：用 pytest 写测试用例
运行方法：在终端里执行  pytest test_httpbin.py -v
"""

import requests

BASE = "https://httpbin.org"


def test_simple_get():
    """测试1：简单 GET 返回 200"""
    r = requests.get(f"{BASE}/get")
    assert r.status_code == 200


def test_get_with_params():
    """测试2：GET 带参数，服务端能正确收到"""
    r = requests.get(f"{BASE}/get", params={"name": "石冠华", "age": 28})
    assert r.status_code == 200
    assert r.json()["args"]["name"] == "石冠华"
    assert r.json()["args"]["age"] == "28"


def test_post_json():
    """测试3：POST 发送 JSON，服务端回显一致"""
    payload = {"user": "shi", "pwd": "123"}
    r = requests.post(f"{BASE}/post", json=payload)
    assert r.status_code == 200
    assert r.json()["json"] == payload


def test_custom_header():
    """测试4：自定义请求头能正确发送"""
    r = requests.get(f"{BASE}/headers", headers={"X-Token": "abc123"})
    assert r.status_code == 200
    assert r.json()["headers"]["X-Token"] == "abc123"


def test_status_404():
    """测试5：请求不存在的路径返回 404"""
    r = requests.get(f"{BASE}/status/404")
    assert r.status_code == 404
