# <https://projecteuler.net/problem=816>
# <p>We create an array of points  $P_n$ in a two dimensional plane using the following random number generator:<br>
# $s_0=290797$<br>
# $s_{n+1}={s_n}^2 \bmod 50515093$
# <br> <br>
# $P_n=(s_{2n},s_{2n+1})$</p>
# <p>
# Let $d(k)$  be the shortest distance of any two (distinct) points among $P_0, \cdots, P_{k - 1}$.<br>
# E.g. $d(14)=546446.466846479$.
# </p>
# <p>
# Find $d(2_000_000)$. Give your answer rounded to $9$ places after the decimal point.
# </p>
# Notes:
#  - Shortest distance
#    - <https://stackoverflow.com/a/61981008/4769802>  
#    - <https://en.wikipedia.org/wiki/Closest_pair_of_points_problem>
#    - expected O(n) Rabin Lipton Closest Pair
#    - <https://stackoverflow.com/questions/5009423/rabins-nearest-neighbor-closest-pair-of-points-algorithm>
#    - <https://rjlipton.com/2009/03/01/rabin-flips-a-coin/>
#    - <https://ecommons.cornell.edu/server/api/core/bitstreams/ff0fc914-dd9f-4cee-9ff1-2f9775cff490/content>
#    - <https://www.cs.umd.edu/~samir/grant/cp.pdf>
#  - Check the period of the random number sequence

import math
import itertools
import time
import random

def rabin_lipton_shortest_distance(points):
    if len(points) < 3:
        return distance(points[0],points[1])
    minimum_guess = sampled_shortest_distance(points)
    first_buckets = generate_buckets(minimum_guess, points)
    approximate_minimum = get_shortest_distance_from_buckets(minimum_guess, first_buckets)
    return approximate_minimum

def get_shortest_distance_from_buckets(min_distance, buckets):
    for key, pnts in buckets.items():
        if len(pnts) > 1:
            min_distance = min(min_distance, rabin_lipton_shortest_distance(pnts))
    return min_distance

def sampled_shortest_distance(points):
    sample_size = max(1, int(len(points)**.5))
    sample_distances = map(lambda pts: distance(pts[0], pts[1]), [ random.sample(points, 2) for i in range(sample_size) ])
    return min(sample_distances)

def generate_buckets(interval_size, points):
    buckets = {}
    for point in points:
        x = point[0] // interval_size
        y = point[1] // interval_size
        bucket = buckets.get((x,y), [])
        buckets[x,y] = bucket + [point]
    return buckets

def test_rabin_lipton_shortest_distance():
    a = [0,0]
    b = [0,1]
    assert 1 == rabin_lipton_shortest_distance([a,b])
    a = [1,1]
    b = [0,0]
    assert 2**.5 == rabin_lipton_shortest_distance([a,b])
    a = [0,0]
    b = [0,5]
    c = [0,1]
    assert 1 == rabin_lipton_shortest_distance([a,b,c])

def dumb_shortest_distance(points):
    return min(map(lambda pnts: distance(pnts[0],pnts[1]), itertools.combinations(points,2)))

def test_dumb_shortest_distance():
    a = [0,0]
    b = [0,1]
    assert 1 == dumb_shortest_distance([a,b])
    a = [1,1]
    b = [0,0]
    assert 2**.5 == dumb_shortest_distance([a,b])
    a = [0,0]
    b = [0,5]
    c = [0,1]
    assert 1 == dumb_shortest_distance([a,b,c])


def distance(a, b):
    return math.dist(a,b)

def test_distance():
    a = [0,0]
    b = [0,1]
    assert 1 == distance(a,b)
    a = [0,0]
    b = [0,2]
    assert 2 == distance(a,b)
    a = [0,0]
    b = [1,0]
    assert 1 == distance(a,b)
    a = [1,0]
    b = [0,0]
    assert 1 == distance(a,b)
    a = [0,1]
    b = [0,0]
    assert 1 == distance(a,b)
    a = [0,1]
    b = [0,2]
    assert 1 == distance(a,b)
    a = [1,0]
    b = [2,0]
    assert 1 == distance(a,b)
    a = [1,1]
    b = [0,0]
    assert 2**.5 == distance(a,b)

def d(k):
    point_generator = next_point()
    points = [ next(point_generator) for i in range(k) ]
    return rabin_lipton_shortest_distance(points)

def test_d_works_with_small_stuff():
    point_generator = next_point()
    assert distance(next(point_generator), next(point_generator)) == d(2)
    assert 546446.466846479 == d(14)
    assert 14759.650571744576 == d(500)

def test_d_works_with_real_values():
    # assert 644.1311978160971 == d(10_000)
    # assert 594.461941590881 == d(100_000)
    # assert 51.22499389946279 == d(1_000_000)
    assert 20.8806130178211 == d(2_000_000)

def next_point():
    generator = next_s()
    while True:
        yield [ next(generator), next(generator) ]

def test_next_point_works_with_real_values():
    generator = next_point()
    [ next(generator) for i in range(4_000_000) ]

def test_next_point():
    point_generator = next_point()
    assert [290797, 629527] == next(point_generator)
    assert [13339144, 15552512] == next(point_generator)

def next_s():
    last_s = 290797
    yield last_s
    while True:
        last_s **= 2
        last_s %= 50515093
        yield last_s

def test_next_s_works_with_real_values():
    generator = next_s()
    [ next(generator) for i in range(4_000_000) ]

def test_next_s():
    generator = next_s()
    assert 290797 == next(generator)
    assert 629527 == next(generator)
    assert 13339144 == next(generator)
    assert 15552512 == next(generator)
