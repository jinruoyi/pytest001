# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5

#测试用例命名规范
#文件要在test_开头，或者_test结尾
#类要以Test开头，方法要以test_开头