from prime_generator import PrimeGenerator


def test_primes_to_max():
    assert PrimeGenerator().primes_to_max(30)[-1] == 29
    assert PrimeGenerator().primes_to_max(30)[0] == 2
    assert PrimeGenerator().primes_to_max(10) == [2, 3, 5, 7]
    assert PrimeGenerator().primes_to_max(97)[-1] == 97
