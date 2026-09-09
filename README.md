# 接口自动化测试（学习项目）

基于 Python + pytest + requests 的接口自动化测试入门项目。

## 技术栈

- Python 3.13
- requests（HTTP 请求库）
- pytest（测试框架）

## 目录结构

| 文件 | 说明 |
|---|---|
| `demo_httpbin.py` | requests 入门演示：GET / POST / 请求头 |
| `test_httpbin.py` | 基础测试用例：断言、状态码、参数 |
| `test_parametrize.py` | 参数化与数据驱动（`@pytest.mark.parametrize`） |

## 运行测试

```bash
# 安装依赖
pip3 install requests pytest

# 运行全部测试
pytest -v
```

## 学习路线

1. requests 发请求 → 2. pytest 写断言 → 3. 参数化 → 4. 封装成框架（进行中）
