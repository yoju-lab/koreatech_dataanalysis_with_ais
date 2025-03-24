import pytest
from howtouse_copilot import is_prime, primes_between

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(-1) == False

def test_primes_between():
    assert primes_between(1, 10) == [2, 3, 5, 7]
    assert primes_between(10, 20) == [11, 13, 17, 19]
    assert primes_between(20, 30) == [23, 29]
    assert primes_between(0, 1) == []
    assert primes_between(-10, 10) == [2, 3, 5, 7]
