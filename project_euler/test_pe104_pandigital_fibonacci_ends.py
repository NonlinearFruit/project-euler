# <https://projecteuler.net/problem=104>
# <p>The Fibonacci sequence is defined by the recurrence relation:</p>
# <blockquote>$F_n = F_{n - 1} + F_{n - 2}$, where $F_1 = 1$ and $F_2 = 1$.</blockquote>
# <p>It turns out that $F_{541}$, which contains $113$ digits, is the first Fibonacci number for which the last nine digits are $1$-$9$ pandigital (contain all the digits $1$ to $9$, but not necessarily in order). And $F_{2749}$, which contains $575$ digits, is the first Fibonacci number for which the first nine digits are $1$-$9$ pandigital.</p>
# <p>Given that $F_k$ is the first Fibonacci number for which the first nine digits AND the last nine digits are $1$-$9$ pandigital, find $k$.</p>
# 
# Notes:
# - https://www.math.net/list-of-fibonacci-numbers
# - Truncating after 9 digits will allow for finding all last-digit pandigital fibbies possible
# - When the kth fibby is last-digit pandigital, then use k to calculate the full fibby
# - Check for first-digit pandigital-ness
# - Bake until done

import sys
import functools
import pytest

def first_digit_and_last_digit_pandigital_fibbie_generator(pandigitalness = 9):
    last_digit_pandigital_fibbie_generator = index_of_last_digit_pandigital_fibbie_generator(pandigitalness)
    while True:
        index = next(last_digit_pandigital_fibbie_generator)
        fibbie = nth_fibbie(index)
        if is_first_digit_pandigital(fibbie, pandigitalness):
            yield index

@pytest.mark.skip(reason="1.49s to solve")
def test_first_digit_and_last_digit_pandigital_fibbie_generator():
    two_pan_fibbie_generator = first_digit_and_last_digit_pandigital_fibbie_generator(2)
    assert 8 == next(two_pan_fibbie_generator) # F(n) == 21
    assert 721 == next(two_pan_fibbie_generator)
    # five_pan_fibbie_generator = first_digit_and_last_digit_pandigital_fibbie_generator(5)
    # assert 503214 == next(five_pan_fibbie_generator)
    nine_pan_fibbie_generator = first_digit_and_last_digit_pandigital_fibbie_generator(9)
    assert 329468 == next(nine_pan_fibbie_generator)

def index_of_last_digit_pandigital_fibbie_generator(pandigitalness = 9):
    modulus = 10 ** pandigitalness
    penultimate_fibbie = 1
    last_fibbie = 0
    n = 0
    while True:
        n += 1
        new_fibbie = (last_fibbie + penultimate_fibbie) % modulus
        penultimate_fibbie = last_fibbie
        last_fibbie = new_fibbie
        if is_last_digit_pandigital(new_fibbie, pandigitalness):
            yield n

def test_index_of_last_digit_pandigital_fibbie_generator():
    assert 1 == next(index_of_last_digit_pandigital_fibbie_generator(1)) # F(n) = 1
    two_pan_fibbie_generator = index_of_last_digit_pandigital_fibbie_generator(2)
    assert 8 == next(two_pan_fibbie_generator) # F(n) = 21
    assert 79 == next(two_pan_fibbie_generator) # F(n) = 14472334024676221
    assert 262 == next(index_of_last_digit_pandigital_fibbie_generator(3)) # F(n) = 2542592393026885507715496646813780220945054040571721231
    assert 307 == next(index_of_last_digit_pandigital_fibbie_generator(4))
    assert 541 == next(index_of_last_digit_pandigital_fibbie_generator(9))

# Helper for calculating the nth Fibonacci
@functools.cache
def powLF(n):
    if n == 1:     return (1, 1)
    L, F = powLF(n//2)
    L, F = (L**2 + 5*F**2) >> 1, L*F
    if n & 1:
        return ((L + 5*F)>>1, (L + F) >>1)
    else:
        return (L, F)

# Gives the nth Fibonacci Number
# 1==1th, 1==2nd, 2==3rd, ...
# https://gist.github.com/NonlinearFruit/ef371219d6f14b6f519faa13a7325b0b
def nth_fibbie(n):
    if n & 1:
        return powLF(n)[1]
    else:
        L, F = powLF(n // 2)
        return L * F

def test_nth_fibbie_examples():
    assert 1 == nth_fibbie(1)
    assert 1 == nth_fibbie(2)
    assert 2 == nth_fibbie(3)
    assert 3 == nth_fibbie(4)
    assert 5 == nth_fibbie(5)
    assert 354224848179261915075 == nth_fibbie(100)

def is_last_digit_pandigital(x, pandigitalness = 9):
    """
    x is the number to check for pandigitalness.
    pandigitalness is the number of pandigits to look for.
    eg: is_last_digit_pandigital(131, 1) == True # Checks if x ends with 1
    eg: is_last_digit_pandigital(131, 2) == False # Checks if x ends with 1 and 2 (any order)
    eg: is_last_digit_pandigital(112, 2) == True # Checks if x ends with 1 and 2 (any order)
    eg: is_last_digit_pandigital(213, 3) == True # Checks if x ends with 1, 2 and 3 (any order)
    """
    return set(str(x)[-pandigitalness:]) == pandigital_sets[pandigitalness]

def test_last_digit_pandigital_examples():
    assert not is_last_digit_pandigital(130,1)
    assert not is_last_digit_pandigital(131,9)
    assert is_last_digit_pandigital(21,2)
    assert is_last_digit_pandigital(131,1)
    assert not is_last_digit_pandigital(131,2)
    assert is_last_digit_pandigital(112,2)
    assert is_last_digit_pandigital(213,3)
    assert not is_last_digit_pandigital(111,3)

# https://stackoverflow.com/a/75162528/4769802
sys.set_int_max_str_digits(0)
pandigital_sets = [
    None,
    set("1"),
    set("12"),
    set("123"),
    set("1234"),
    set("12345"),
    set("123456"),
    set("1234567"),
    set("12345678"),
    set("123456789"),
]
def is_first_digit_pandigital(x, pandigitalness = 9):
    return set(str(x)[:pandigitalness]) == pandigital_sets[pandigitalness]

def test_is_first_digit_pandigital_examples():
    assert is_first_digit_pandigital(21, 2)
    assert is_first_digit_pandigital(198, 1)
    assert not is_first_digit_pandigital(2, 1)
    assert is_first_digit_pandigital(2198, 2)
    assert is_first_digit_pandigital(987654321, 9)
    assert not is_first_digit_pandigital(987654320, 9)
    assert not is_first_digit_pandigital(9876543201, 9)

if __name__ == "__main__":
    args = sys.argv
    # args[0] = current file
    # args[1] = function name
    # args[2:] = function args : (*unpacked)
    print(globals()[args[1]](*args[2:]))
