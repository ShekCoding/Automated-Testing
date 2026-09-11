# -*- coding: utf-8 -*-
"""
第三课：封装 —— 用例只关心"测什么"
运行：pytest test_encapsulated.py -v

对比一下：这里不再写 requests.get、不再写 BASE_URL，
全部来自 common/http_client.py，用例变得非常干净。
"""

import pytest
from common.http_client import api_get, api_post, assert_status


def test_simple_get():
    r = api_get("/get")
    assert_status(r)


def test_get_with_params():
    r = api_get("/get", params={"name": "石冠华", "age": 28})
    assert_status(r)
    assert r.json()["args"]["name"] == "石冠华"


def test_post_json():
    payload = {"user": "shi", "pwd": "123"}
    r = api_post("/post", json=payload)
    assert_status(r)
    assert r.json()["json"] == payload


@pytest.mark.parametrize("code", [200, 400, 404])
def test_status_codes(code):
    r = api_get(f"/status/{code}")
    assert_status(r, code)
