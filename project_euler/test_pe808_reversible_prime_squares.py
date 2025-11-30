# <https://projecteuler.net/problem=808>
# <p>
# Both $169$ and $961$ are the square of a prime. $169$ is the reverse of $961$.
# </p>
# <p>
# We call a number a <dfn>reversible prime square</dfn> if:</p>
# <ol>
# <li>It is not a palindrome, and</li>
# <li>It is the square of a prime, and</li>
# <li>Its reverse is also the square of a prime.</li>
# </ol>
# <p>
# $169$ and $961$ are not palindromes, so both are reversible prime squares.
# </p>
# <p>
# Find the sum of the first $50$ reversible prime squares.
# </p>

import pytest

# Source - https://stackoverflow.com/a/3035188
# Posted by Robert William Hanks, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-29, License - CC BY-SA 4.0
import numpy
def primes_from_2_to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n//3 + (n%6==2), dtype=bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

def test_gets_primes():
    primes = primes_from_2_to(10)
    assert 1 not in primes
    assert 2 in primes
    assert 3 in primes
    assert 4 not in primes
    assert 5 in primes
    assert 6 not in primes
    assert 7 in primes
    assert 8 not in primes
    assert 9 not in primes
    assert 10 not in primes

def test_respects_the_limit():
    assert 11 not in primes_from_2_to(10)

# Source - https://stackoverflow.com/a/24953539
# Posted by Alberto, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-29, License - CC BY-SA 3.0
def reverse_number(n):
    r = 0
    while n > 0:
        r *= 10
        r += n % 10
        n //= 10
    return r

def test_reverses_numbers():
    assert 0 == reverse_number(0)
    assert 1 == reverse_number(1)
    assert 12 == reverse_number(21)
    assert 123 == reverse_number(321)


from random import randrange

# Source - https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python
# Will give correct answers for n less than 341550071728321 and then reverting to the probabilistic form
def is_probably_prime(n, _precision_for_huge_n=16):
    if n in _known_primes:
        return True
    if any((n % p) == 0 for p in _known_primes) or n in (0, 1):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])

def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite

_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_probably_prime(x)]

def test_finds_primes():
    assert is_probably_prime(2)
    assert is_probably_prime(23)
    assert is_probably_prime(239)
    assert is_probably_prime(2399)

def test_finds_composites():
    assert not is_probably_prime(1)
    assert not is_probably_prime(12)
    assert not is_probably_prime(124)
    assert not is_probably_prime(1248)

def is_integer(n):
    return n % 1 == 0

def test_finds_integers():
    assert is_integer(0)
    assert is_integer(1)
    assert is_integer(2)
    assert is_integer(3)

def test_finds_non_integers():
    assert not is_integer(0.1)
    assert not is_integer(1.01)
    assert not is_integer(11.001)
    assert not is_integer(111.00000000001)

from math import isqrt, sqrt

def reversible_prime_squares_less_than(n):
    reversible_prime_squares = []
    max = isqrt(n) + 1
    for p in primes_from_2_to(max):
        square = p * p
        reverse = reverse_number(square)
        if square == reverse:
            continue
        root = sqrt(reverse)
        if is_integer(root) and is_probably_prime(int(root)):
            reversible_prime_squares.append(square)
    return reversible_prime_squares

def test_finds_reversible_prime_squares():
    squares = reversible_prime_squares_less_than(1000)
    assert 169 in squares
    assert 961 in squares

def test_does_not_include_palindromes():
    assert 121 not in reversible_prime_squares_less_than(130)

@pytest.mark.skip(reason="lots of seconds to solve")
def test_sum_first_50_reversible_prime_squares():
    # assert 2 == len(reversible_prime_squares_less_than(1000))
    # assert 4 == len(reversible_prime_squares_less_than(10**6))
    # assert 12 == len(reversible_prime_squares_less_than(10**9))
    # assert 32 == len(reversible_prime_squares_less_than(10**14))
    # assert 50 == len(reversible_prime_squares_less_than(10**16))
    assert 3807504276997394 == sum(reversible_prime_squares_less_than(10**16))
