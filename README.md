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
├── pytest.ini              # pytest 配置（重试、默认参数、收集目录）
├── conftest.py             # 共享 fixture + --env 多环境参数
├── requirements.txt        # 依赖清单
├── common/                 # 封装层
│   ├── http_client.py      # 统一请求方法 + 断言
│   └── config.py           # 多环境配置
├── tests/                  # 用例层
│   ├── test_httpbin.py       # 基础用例：GET / POST / 请求头 / 状态码
│   ├── test_parametrize.py   # 参数化与数据驱动
│   ├── test_encapsulated.py  # 封装后的用例（调用 common/http_client.py）
│   ├── test_fixture.py       # fixture 与 Session 复用
│   ├── test_env.py           # 多环境切换
│   └── test_jsonpath.py      # jsonpath 断言
├── examples/               # 入门演示
│   ├── demo_httpbin.py       # requests 基础用法
│   └── test_rerun_demo.py    # 失败重试演示
└── README.md
```

## 快速开始

```bash
# 1. 安装依赖
pip3 install -r requirements.txt

# 2. 运行全部测试（已配置失败重试 + 详细输出）
pytest

# 3. 生成测试报告（手动）
pytest --html=report.html --self-contained-html
# 想每次自动生成，把下面这行写进 pytest.ini 的 addopts：
# addopts = -v --html=report.html --self-contained-html
```

## 框架设计

- **分层**：用例层（`tests/`）与封装层（`common/`）分离，用例只关心"测什么"；
- **配置集中**：域名、重试规则等集中在 `pytest.ini` / `common/config.py`，换环境只改一处；
- **稳定性**：失败自动重试（默认 2 次、间隔 1 秒），应对网络抖动；
- **报告**：一键生成 HTML 可视化报告。

## 学习路线

1. requests 发请求 → 2. pytest 断言 → 3. 参数化 → 4. 封装分层 → 5. 失败重试 → 6. 测试报告
