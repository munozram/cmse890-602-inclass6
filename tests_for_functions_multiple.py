import pytest
from example_functions import my_adder, my_thermo_stat, have_digits

@pytest.mark.parametrize("a,b,c,sum", [(3, 5, 15, 23), (2, 4, 8, 14), (6, 9, 54, 69)])
def test_adder(a,b,c,sum):
    assert my_adder(a,b,c) == sum

@pytest.mark.parametrize("temp,desired,status", [(32,60,'Heat'), (83,75,'AC'), (65,70,'off'), (74,72,'off')])
def test_thermo(temp,desired,status):
    assert my_thermo_stat(temp,desired) == status

@pytest.mark.parametrize("string,check", [('adshfb',0), ('2asjbd',1), ('als asdkn9',1)])
def test_digits(string,check):
    assert have_digits(string) == check