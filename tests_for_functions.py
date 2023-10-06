
from example_functions import my_adder, my_thermo_stat, have_digits

def test_adder():
    assert my_adder(1,2,3) == 6

def test_thermo():
    assert my_thermo_stat(70,76) == 'Heat'

def test_digits():
    assert have_digits('abc1def') == 1