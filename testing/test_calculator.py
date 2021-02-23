import sys
import yaml
from pytestmmm.pythoncode.Calculator import Calculator

sys.path.append('..')
print(sys.path)
file = open("data/calculator_data.yml")
data = yaml.full_load(file)
test_data = data["add"]["test_data"]
print(test_data)

class TestCalc:
    calc = Calculator()
    def setup(self):
        print("开始计算")
    def teardown(self):
        print("计算结束")
    def test_add(self):
        for testdata in test_data:
            assert testdata[2] == self.calc.add(testdata[0],testdata[1])
    # def test_div(self):
    #     # assert 3 == self.calc.div(6,2)
    #     assert "error" == self.calc.div(6,0)
