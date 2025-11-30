# <https://projecteuler.net/problem=751>
# <p>A non-decreasing sequence of integers $a_n$ can be generated from any positive real value $\theta$ by the following procedure:
# $$\begin{align}
# \begin{split}
# b_1 &amp;= \theta \\
# b_n &amp;= \left\lfloor b_{n-1} \right\rfloor \left(b_{n-1} - \left\lfloor b_{n-1} \right\rfloor + 1\right)~~~\forall ~ n \geq 2 \\
# a_n &amp;= \left\lfloor b_{n} \right\rfloor
# \end{split}
# \end{align}$$
# Where $\left\lfloor \cdot \right\rfloor$ is the floor function.</p>
# 
# <p>For example, $\theta=2.956938891377988...$ generates the Fibonacci sequence: $2, 3, 5, 8, 13, 21, 34, 55, 89, ...$</p>
# 
# <p>The <i>concatenation</i> of a sequence of positive integers $a_n$ is a real value denoted $\tau$ constructed by concatenating the elements of the sequence after the decimal point, starting at $a_1$: $a_1.a_2a_3a_4...$</p>
# 
# <p>For example, the Fibonacci sequence constructed from $\theta=2.956938891377988...$ yields the concatenation $\tau=2.3581321345589...$ Clearly, $\tau \neq \theta$ for this value of $\theta$.</p>
# 
# <p>Find the only value of $\theta$ for which the generated sequence starts at $a_1=2$ and the concatenation of the generated sequence equals the original value: $\tau = \theta$. Give your answer rounded to $24$ places after the decimal point.</p>
# Notes:
# - Since it starts with 2, a1 is 2 and theta must round down to 2
# - a2 is either 2 or 3, depending on whether or not the decimal places round up or down (since they get doubled)
# - Since the tenths place in theta is a 2 or 3, it must round down. So a2 is 2.
# - a3 is either 2 or 3, depending on whether or not the decimal places round up or down (since they get doubled)
# - Theta is currently 2.2, so b1 = 2.2, b2 = 2.4 (or 2.5). In either case, a3 must be 2
# - b3 must be greater than (or equal to) 2.5. So a4 must be 3
# - Theta is now 2.223

from math import floor
from decimal import *

def b(theta, n):
    if n == 1: return theta
    solution = theta
    while n > 1:
        solution = floor(solution) * (solution - floor(solution) + 1)
        n -= 1
    return solution

def test_b_works():
    assert 2 == b(2, 1)
    assert Decimal('2.4') == b(Decimal('2.2'), 2)

def a_sequence(theta):
    solution = str(floor(b(theta,1))) + "."
    for i in range(2,25):
        solution += str(floor(b(theta,i)))
    return solution

def theta_generator(theta=2):
    stringy_theta = str(theta)
    if len(stringy_theta) >= 26:
        return theta
    solution = a_sequence(theta)
    stringy_solution = str(solution)
    if stringy_solution.startswith(stringy_theta):
        next = stringy_solution[len(stringy_theta)]
        if next == ".":
            next += stringy_solution[len(stringy_theta) + 1]
        return theta_generator(Decimal(stringy_theta + next))
    else:
        return -1

def test_works():
    assert Decimal('2.223561019313554106173177') == theta_generator()
