# 接口自动化测试框架（学习项目）

基于 **Python + pytest + requests** 搭建的接口自动化测试框架，具备请求封装、参数化、失败重试、测试报告等能力。

## 技术栈

| 组件 | 用途 |
|---|---|
| Python 3.13 | 开发语言 |
| requests | HTTP 请求库 |
| pytest | 测试框架（用例、断言、参数化） |
| pytest-html | 生成可视化测试报告 |
| pytest-rerunfailures | 失败自动重试，降低网络抖动误报 |

## 项目结构

```
.
├── pytest.ini            # pytest 配置（重试规则、默认参数）
├── common.py             # 封装层：统一请求方法 + 断言
├── demo_httpbin.py       # 入门演示：requests 基础用法
├── test_httpbin.py       # 基础用例：GET / POST / 请求头 / 状态码
├── test_parametrize.py   # 参数化与数据驱动
├── test_encapsulated.py  # 封装后的用例（调用 common.py）
├── test_rerun_demo.py    # 失败重试演示
└── README.md
```

## 快速开始

```bash
# 1. 安装依赖
pip3 install requests pytest pytest-html pytest-rerunfailures

# 2. 运行全部测试（已配置失败重试 + 详细输出）
pytest

# 3. 生成测试报告
pytest --html=report.html --self-contained-html
```

## 框架设计

- **分层**：用例层（`test_*.py`）与封装层（`common.py`）分离，用例只关心"测什么"；
- **配置集中**：域名、重试规则等集中在 `pytest.ini` / `common.py`，换环境只改一处；
- **稳定性**：失败自动重试（默认 2 次、间隔 1 秒），应对网络抖动；
- **报告**：一键生成 HTML 可视化报告。

## 学习路线

1. requests 发请求 → 2. pytest 断言 → 3. 参数化 → 4. 封装分层 → 5. 失败重试 → 6. 测试报告
