INCLUSIVE = 1


class PrimeGenerator:
    def primes_to_max(self, end):
        not_primes = set()
        result = []
        for num in range(2, end + INCLUSIVE):
            if not (num in not_primes):
                result.append(num)
                for i in range(2 * num, end + INCLUSIVE, num):
                    not_primes.add(i)
        return result
