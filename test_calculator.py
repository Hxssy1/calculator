from calculator1 import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_divide():
    assert divide(6, 2) == 3

def test_multiply():
    assert multiply(2, 4) == 8

def test_subtract():
    assert subtract(9, 5) == 4

def test_divide_uneven():
    #arrange 
    a, b = 5, 2
    #act
    result = divide(a, b)
    #assert
    assert result == 2.5