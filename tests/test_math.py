import pytest


def test_one_plus_one():
    assert 1 + 1 == 2


def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c


# -------------------------------------------------------------------------------------------------
# A test function that verifies an exception
# -------------------------------------------------------------------------------------------------


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
    assert 'division by zero' in str(e.value)


# -------------------------------------------------------------------------------------------------
#  multiplication
# -------------------------------------------------------------------------------------------------

# We could multiply two positive integers.
#
# We could test identity by multiplying any number by one.
#
# We could test the zero property by multiplying any number by zero.
#
# We can multiply a positive by a negative.
#
# We could test negative numbers multiplied by negative numbers.
#
# We could also multiply floating point numbers instead of integers.

# def test_multiply_two_positive_ints():
#   assert 2 * 3 == 6
#
# def test_multiply_identity():
#   assert 1 * 99 == 99
#
# def test_multiply_zero():
#   assert 0 * 100 == 0

products = [
    (2, 3, 6),  # positive integers
    (1, 99, 99),  # identity
    (0, 99, 0),  # zero
    (3, -4, -12),  # positive by negative
    (-5, -5, 25),  # negative by negative
    (2.5, 6.7, 16.75)  # floats
]


@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product
