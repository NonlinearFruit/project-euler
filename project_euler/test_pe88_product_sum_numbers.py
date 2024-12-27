# <https://projecteuler.net/problem=88>
# <p>A natural number, $N$, that can be written as the sum and product of a given set of at least two natural numbers, $\{a_1, a_2, \dots, a_k\}$ is called a product-sum number: $N = a_1 + a_2 + \cdots + a_k = a_1 \times a_2 \times \cdots \times a_k$.</p>
# <p>For example, $6 = 1 + 2 + 3 = 1 \times 2 \times 3$.</p>
# <p>For a given set of size, $k$, we shall call the smallest $N$ with this property a minimal product-sum number. The minimal product-sum numbers for sets of size, $k = 2, 3, 4, 5$, and $6$ are as follows.</p>
# <ul style="list-style-type:none;">
# <li>$k=2$: $4 = 2 \times 2 = 2 + 2$</li>
# <li>$k=3$: $6 = 1 \times 2 \times 3 = 1 + 2 + 3$</li>
# <li>$k=4$: $8 = 1 \times 1 \times 2 \times 4 = 1 + 1 + 2 + 4$</li>
# <li>$k=5$: $8 = 1 \times 1 \times 2 \times 2 \times 2 = 1 + 1 + 2 + 2 + 2$</li>
# <li>$k=6$: $12 = 1 \times 1 \times 1 \times 1 \times 2 \times 6 = 1 + 1 + 1 + 1 + 2 + 6$</li></ul>
# <p>Hence for $2 \le k \le 6$, the sum of all the minimal product-sum numbers is $4+6+8+12 = 30$; note that $8$ is only counted once in the sum.</p>
# <p>In fact, as the complete set of minimal product-sum numbers for $2 \le k \le 12$ is $\{4, 6, 8, 12, 15, 16\}$, the sum is $61$.</p>
# <p>What is the sum of all the minimal product-sum numbers for $2 \le k \le 12000$?</p>
# 
# Notes:
# - https://www.ivl-projecteuler.com/overview-of-problems/40-difficulty/problem-88
# - https://blog.dreamshire.com/project-euler-88-solution/
# - https://docs.python.org/3/library/functools.html
# - k is the length of the list of natural numbers which are multiplied and added
# - N is the result of adding the list of natural numbers
# - Number of Ones = Product of Factors - Sum of Factors
# - k = Number of Ones + Number of Factors
from operator import mul
from functools import reduce

def sum_of_minimal_product_sum_numbers(maxK):
    minProdSumNums = get_minimal_product_sum_numbers(maxK)
    return sum(set(minProdSumNums.values()))

def test_example_case():
    assert 30 == sum_of_minimal_product_sum_numbers(6)

def test_real_k_case():
    # assert 890 == sum_of_minimal_product_sum_numbers(60)
    # assert 39072 == sum_of_minimal_product_sum_numbers(600)
    # assert 93063 == sum_of_minimal_product_sum_numbers(1000)
    assert 7587457 == sum_of_minimal_product_sum_numbers(12000)

def get_minimal_product_sum_numbers(maxK, oldFactors = [], minProdSumNums = {}):
    if len(oldFactors) > 12:
        return minProdSumNums
    start = get_largest_factor(oldFactors) or 2
    for i in range(start, maxK + 1):
        factors = oldFactors + [i]
        N = reduce(mul, factors, 1)
        K = k(N, factors)
        if K > maxK:
            break
        if K > 1 and N < minProdSumNums.get(K, N + 1):
            minProdSumNums[K] = N
        minProdSumNums = get_minimal_product_sum_numbers(maxK, factors, minProdSumNums)
    return minProdSumNums

def test_getting_minimal_product_sum_numbers_works():
    assert {2:4, 3:6} == get_minimal_product_sum_numbers(3, [], {})

def get_largest_factor(sortedFactorList):
    return sortedFactorList[-1] if sortedFactorList else None

def k(N, factors):
    return len(factors) + number_of_ones(N, factors)

def test_k():
    assert 2 == k(4, [2, 2])
    assert 3 == k(6, [2, 3])

def number_of_ones(N, factors):
    return N - sum(factors)

def test_number_of_ones():
    assert 0 == number_of_ones(4, [2, 2])
    assert 1 == number_of_ones(6, [2, 3])
