# -*- coding: utf-8 -*-
"""
第五课：fixture（前置/后置）与 Session 复用
运行：pytest test_fixture.py -v -s
（加 -s 才能看到 print 输出）
"""

import pytest
import requests


# 1. 默认 function 级 fixture：每个用例都重新准备一次
@pytest.fixture
def test_data():
    print("\n  [fixture] 准备测试数据")   # ← setup（类似构造函数）
    data = {"user": "shi", "pwd": "123"}
    yield data                          # ← yield 是分界
    print("\n  [fixture] 清理测试数据")   # ← teardown（类似析构函数）


def test_use_data(test_data):
    print(f"  用例拿到数据: {test_data}")
    assert test_data["user"] == "shi"


# 2. session 级 fixture：整个测试会话只创建一次 Session，复用 TCP 连接
@pytest.fixture(scope="session")
def client():
    """复用同一个 requests.Session，避免每次新建连接（性能优化）"""
    s = requests.Session()
    yield s          # 所有用例共用同一个 s
    s.close()        # 全部测试结束后才关闭


def test_get(client):
    r = client.get("https://httpbin.org/get")
    assert r.status_code == 200


def test_post(client):
    r = client.post("https://httpbin.org/post", json={"a": 1})
    assert r.status_code == 200
