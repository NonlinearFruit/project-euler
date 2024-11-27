# <https://projecteuler.net/problem=800>
# <p>
# An integer of the form $p^q q^p$ with prime numbers $p \neq q$ is called a <dfn>hybrid-integer</dfn>.<br>
# For example, $800 = 2^5 5^2$ is a hybrid-integer.
# </p>
# <p>
# We define $C(n)$ to be the number of hybrid-integers less than or equal to $n$.<br>
# You are given $C(800) = 2$ and $C(800^{800}) = 10790$.
# </p>
# <p>
# Find $C(800800^{800800})$.
# </p>
# Notes:
# - sqrt(800800^800800) = HUGE
# - log2(800800^800800) < 1.6 x 10^7
#   - Largest prime less than 1.6 x 10^7 is 1,599,9989
#   - Number of primes < 1.6 x 10^7 is 1,031,130
# - log3(800800^800800) < 1.0 x 10^7
#   - Largest prime less than 1.0 x 10^7 is 9999_991
#   - Number of primes < 1.0 x 10^7 is 664579
# - log5(800800^800800) < 6.8 x 10^6
#   - Largest prime less than is ??
#   - Number of primes less than  is ??
# - log7(800800^800800) < 5.6 x 10^6
#   - Largest prime less than is ??
#   - Number of primes less than  is ??
# - p^q * q^p = h
#   - log(p^q) + log(q^p) = log(h)
#   - q*log(p) + p*log(q) = log(h)
#   - Assume p = 2 and use log base q
#   - q*logq(2) + 2*1 = logq(h)
#   - q = 15999989
#   - 668574.6 =(?) logq(800800^800800) =  656227.6

import pytest
import numpy
import math
from decimal import Decimal

# <https://stackoverflow.com/a/3035188>
def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n//3 + (n%6==2), dtype=bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

def test_can_get_primes():
    primes = primesfrom2to(16000000)
    assert len(primes) == 1031130
    assert 15999989 == primes[-1]

def C(n):
    largest_prime = math.ceil(log(n, 2))
    primes = primesfrom2to(largest_prime)
    numberOfPrimes = len(primes)
    print(numberOfPrimes)
    count = 0
    for i in range(numberOfPrimes):
        p = primes[i]
        nLog = log(n, p)
        count += max(binary_search(primes, nLog, lambda q: p * log(q, p) + q) - i, 0)
        if i % 100000 == 0:
            print(i)
    return count

def log(number, base):
    return math.log(number, base)

def binary_search(a, nLog, function):
    lo = 0
    hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        midval = function(a[mid])
        if midval < nLog:
            lo = mid + 1
        elif midval > nLog:
            hi = mid
        else:
            return mid
    return hi - 1

@pytest.mark.skip(reason="48s to solve")
def test_C_works_for_examples():
    """You are given $C(800) = 2$ and $C(800^{800}) = 10790$."""
    # assert C(800) == 2
    # assert C(800**800) == 10790
    # assert C(8008**8008) == 440302
    # assert C(80080**8008) == 621290
    # assert C(80080**80080) == 23036066
    # assert C(800800**80080) == 31110609
    assert C(800800**800800) == 1412403576

