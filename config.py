# -*- coding: utf-8 -*-
"""多环境配置：不同环境对应不同的基础地址"""

ENVIRONMENTS = {
    "test": "https://httpbin.org",              # 测试环境（真实可用）
    "staging": "https://staging.example.com",   # 预发环境（示例地址）
    "prod": "https://api.example.com",          # 生产环境（示例地址）
}
