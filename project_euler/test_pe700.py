# <https://projecteuler.net/problem=700>
# <p>Leonhard Euler was born on 15 April 1707.</p>
# 
# <p>Consider the sequence 1504170715041707<var>n</var> mod 4503599627370517.</p>
# 
# <p>An element of this sequence is defined to be an Eulercoin if it is strictly smaller than all previously found Eulercoins.</p>
# 
# <p>For example, the first term is 1504170715041707 which is the first Eulercoin.  The second term is 3008341430083414 which is greater than 1504170715041707 so is not an Eulercoin.  However, the third term is 8912517754604 which is small enough to be a new Eulercoin.</p>
# 
# <p>The sum of the first 2 Eulercoins is therefore 1513083232796311.</p>
# 
# <p>Find the sum of all Eulercoins.</p>
#
# Notes:
#  1504170715041707 and 4503599627370517 are coprime (the second is prime)
# 
#  Check out Schrage's Method for multiplying in a modulus without getting bigger:
#     https://craftofcoding.wordpress.com/2021/07/05/demystifying-random-numbers-schrages-method/
# 
#  The sequence of coins will start with 1504170715041707 and end with 1. Finding the middle bits is the trick
# 
#  Increment by current number until just before topping the modulus. Convert it to a negative number.
#   - Add the negative number to the current number until passes zero.
#   - Use that number as the new negative number.
#   - Repeat
# 
#  Modular multiplicative inverse: pow(1504170715041707, -1, 4503599627370517)
#  Almost helpful: <https://urmaul.com/blog/solution-for-project-euler-problem-700/>

def find_euler_coins(coin = 1504170715041707, modulus = 4503599627370517):
    next_coin = coin - (modulus % coin)
    smaller_coins = [next_coin] if next_coin == 1 else find_euler_coins(next_coin, coin)
    return [coin] + smaller_coins

def test_find_euler_coin_with_real_values():
    coins = find_euler_coins()
    assert 1504170715041707 == coins[0]
    assert 8912517754604 == coins[1]
    assert 578033868113 == coins[4]
    assert 1517913526188578 == sum(coins[:10])
    assert 1517926517777556 == sum(coins)

def test_find_euler_coin_with_small_stuff():
    assert [15, 13, 11, 9, 7, 5, 3, 1] == find_euler_coins(15, 47)
    assert [5, 3, 1] == find_euler_coins(5, 777)
    assert [214, 79, 23, 13, 3, 2, 1] == find_euler_coins(214, 777)


