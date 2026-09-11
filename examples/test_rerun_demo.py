# -*- coding: utf-8 -*-
"""
第四课：失败重试（pytest-rerunfailures）
演示：一个"不稳定"的用例，前两次失败、第三次成功。
运行：pytest test_rerun_demo.py --reruns 2 -v
"""

_counter = 0


def test_flaky_example():
    """模拟不稳定用例：故意失败两次，第三次才通过"""
    global _counter
    _counter += 1
    if _counter < 3:
        assert False, f"第 {_counter} 次运行，模拟网络抖动失败"
    assert True
