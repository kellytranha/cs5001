from prime_generator import PrimeGenerator


def main():
    end = int(input("Prime numbers up to: "))
    print(PrimeGenerator().primes_to_max(end))


main()
