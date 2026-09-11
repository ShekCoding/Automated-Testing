# -*- coding: utf-8 -*-
"""
第六课：多环境配置
运行：pytest test_env.py             # 默认 test 环境
      pytest test_env.py --env=test  # 显式指定环境
"""
import requests


def test_env_base(base_url):
    print(f"\n  当前环境基础地址: {base_url}")
    r = requests.get(f"{base_url}/get")
    assert r.status_code == 200
