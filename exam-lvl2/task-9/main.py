# Implement a Custom Iterator for Prime Numbers
# Objective: Design a class `PrimeIterator` that generates an infinite sequence of prime numbers.
# Parameters:
# - None, but the iterator should handle internal state for generating primes.
# Returns:
# - Prime numbers, one at a time, indefinitely.
# Details:
# - Implement the iterator protocol methods `__iter__()` and `__next__()`.
# - Use a sophisticated method to check for primes to ensure efficiency as numbers grow large.

class PrimeIterator:
    def __init__(self):
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        while not self.is_prime(self.current):
            self.current += 1
        return self.current

    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
# Example:
primes = PrimeIterator()
for _ in range(10):
 print(next(primes))  # Prints the first 10 prime numbers
