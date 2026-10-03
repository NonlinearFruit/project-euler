# <https://projecteuler.net/problem=1005>
# <p>
# There are four lists of increasing primes that sum to $20$:</p>
# 
# <div style="text-align:center;">$ (2, 5, 13) ; (2, 7, 11) ; (3, 17) ; (7, 13) $</div>
# 
# <p>
# The <i>median prime list</i> is defined to be the median of <b>these lists</b> when they are written in lexicographic order (as shown in the example above).<br>
# If there are an even number of lists then disregard the last one and find the median of the rest.</p>
# 
# <p>
# Therefore the median prime list of $20$ is $(2, 7, 11)$.</p>
# 
# <p>
# Find the median prime list of $2026$. Give the last nine digits of the product of the primes.</p>
# 
# Notes:
# - About 310 primes less than 2026

import sys
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

def prime_combinations_that_sum_to(n = 20):
    primes = primesfrom2to(int(n))
    return possible_ways_that_sum_to_max(primes, int(n))

def possible_ways_that_sum_to_max(primes, max, choosen = []):
    solutions = []
    for i in range(0, len(primes)):
        prime = primes[i]
        new_choosen = choosen + [prime]
        new_max = max - prime
        new_primes = primes[i+1:]
        if new_max == 0:
            solutions.append(new_choosen)
            break
        elif new_max <= prime:
            print("-----")
            print(new_max)
            print(new_choosen)
            break
        elif len(new_primes) > 0:
            solutions += possible_ways_that_sum_to_max(new_primes, new_max, new_choosen)
    return solutions

def test_prime_combinations_that_sum_to_n():
    assert [[2, 3]] == prime_combinations_that_sum_to(5)
    assert 4 == len(prime_combinations_that_sum_to(20))
    assert 4660 == len(prime_combinations_that_sum_to(200))

if __name__ == "__main__":
    args = sys.argv
    # args[0] = current file
    # args[1] = function name
    # args[2:] = function args : (*unpacked)
    globals()[args[1]](*args[2:])
