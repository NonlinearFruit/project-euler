# <https://projecteuler.net/problem=932>
# <p>For the year $2025$</p>
# $$2025 = (20 + 25)^2$$
# <p>Given positive integers $a$ and $b$, the concatenation $ab$ we call a $2025$-number if $ab = (a+b)^2$.<br>
# Other examples are $3025$ and $81$.<br>
# Note $9801$ is not a $2025$-number because the concatenation of $98$ and $1$ is $981$.</p>
# 
# <p>
# Let $T(n)$ be the sum of all $2025$-numbers with $n$ digits or less. You are given $T(4) = 5131$.</p>
# 
# <p>
# Find $T(16)$.</p>
# 
# Notes:
# - 0 does not count of b, 100 being (10 + 0)^2 is not included
# - Iterating over the roots from 2 to 10**8 should work

# Fiddling with math 
# - Let x be the square number (eg: 2025)
# - Let y be the root of a square y (eg: 45)
# - Let a be the left hand side of the root sum (eg: 20)
# - Let b be the right hand side of the root sum (eg: 25)
# - Given x = y^2
# - Given y = a + b
# - Given $"($a)($b)" == $"($y)"
# - The number of decimal digits in a number is floor(log b) + 1
# - Let digit_count_of(n): floor(log n) + 1
# - Then x = a*10^digit_count_of(b) + b
# - So b = x - a*10^digit_count_of(b)
# - Substituting gives y = a + x - a*10^digit_count_of(b)
# - y - x = a - a*10^digit_count_of(b)
# - x - y = a*10^digit_count_of(b) - a
# - x - y = a(10^digit_count_of(b) - 1)
# - a = (x - y) / (10^digit_count_of(b) - 1)
# - Since the digit count of b must be a whole number, 10^digit_count_of(b) - 1 must be 1 less than a power of ten
# - x - y must be divisible by 9 or 99 or 999 etc
# - Therefore x - y must be divisible by 9

import pytest
from math import isqrt

def sum_of_2025_numbers_with_digit_count_less_than_or_equal_to(digit_count):
    max = isqrt(10 ** digit_count)
    return sum(
            map(lambda tuple: tuple[2],
                filter(lambda tuple: tuple != None,
                       map(extract_a_and_b,
                           [root for root in range(2, max + 1)]))))

def test_sum_works_with_example():
    assert 5131 == sum_of_2025_numbers_with_digit_count_less_than_or_equal_to(4)
    # assert 587549 == sum_of_2025_numbers_with_digit_count_less_than_or_equal_to(6)
    # assert 176339975 == sum_of_2025_numbers_with_digit_count_less_than_or_equal_to(8)

@pytest.mark.skip(reason="lots of seconds to solve")
def test_sum_works_with_real_number():
    assert 72673459417881349 == sum_of_2025_numbers_with_digit_count_less_than_or_equal_to(16)

def extract_a_and_b(root):
    square = root**2
    diff = square - root
    if diff % 9 != 0:
        return None
    str_square = str(square)
    for digits_in_b in range(1,9):
        base = 10 ** digits_in_b
        b = square % base
        if b == 0:
            continue
        a, a_remainder = divmod(diff, base - 1)
        if a_remainder == 0 and f'{a}{b}' == str_square:
            return a, b, square

def test_a_extracting_works():
    assert 8 == extract_a_and_b(9)[0]
    assert 20 == extract_a_and_b(45)[0]
    assert 30 == extract_a_and_b(55)[0]

def test_b_extracting_works():
    assert 1 == extract_a_and_b(9)[1]
    assert 25 == extract_a_and_b(45)[1]

def test_extracting_fails_when_diff_is_not_a_multiple_of_9():
    assert None == extract_a_and_b(8)

def test_extracting_fails_when_b_is_0():
    assert None == extract_a_and_b(10)
    assert None == extract_a_and_b(100)

def test_extracting_fails_when_b_requires_leading_zeros():
    assert None == extract_a_and_b(99)
