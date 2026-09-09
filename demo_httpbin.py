# -*- coding: utf-8 -*-
"""
httpbin 接口测试入门示例
运行方法：在终端里执行  python3 demo_httpbin.py
"""

import requests

BASE = "https://httpbin.org"


def demo_get():
    """1. 最简单的 GET 请求"""
    print("=" * 40)
    print("1. 简单 GET 请求")
    r = requests.get(f"{BASE}/get")
    print("状态码:", r.status_code)
    print("返回内容:", r.json())


def demo_get_with_params():
    """2. 带参数的 GET 请求"""
    print("=" * 40)
    print("2. 带参数的 GET 请求")
    r = requests.get(f"{BASE}/get", params={"name": "石冠华", "age": 28})
    # args 是 httpbin 回显给你的查询参数
    print("收到的参数:", r.json()["args"])


def demo_post_json():
    """3. POST 请求，发送 JSON 数据"""
    print("=" * 40)
    print("3. POST 请求（发 JSON）")
    r = requests.post(f"{BASE}/post", json={"user": "shi", "pwd": "123"})
    print("状态码:", r.status_code)
    print("回显的 body:", r.json()["json"])


def demo_headers():
    """4. 自定义请求头"""
    print("=" * 40)
    print("4. 自定义请求头")
    r = requests.get(f"{BASE}/headers", headers={"X-Token": "abc123"})
    print("回显的请求头:", r.json()["headers"])


if __name__ == "__main__":
    try:
        demo_get()
        demo_get_with_params()
        demo_post_json()
        demo_headers()
        print("\n全部跑通了！下一步把它写成 pytest 测试用例。")
    except requests.exceptions.ConnectionError:
        print("\n连不上 httpbin.org，可能是网络问题，稍后重试。")
