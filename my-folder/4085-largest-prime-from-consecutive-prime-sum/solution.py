class Solution(object):
    def largestPrime(self, n):
        if n < 2:
            return 0

        isPrime = [False, False] + [True] * (n - 1)

        i = 2
        while i * i <= n:
            if isPrime[i]:
                for j in range(i * i, n + 1, i):
                    isPrime[j] = False
            i += 1

        primes = []
        for i in range(2, n + 1):
            if isPrime[i]:
                primes.append(i)

        total = 0
        largest = 0

        for prime in primes:
            total += prime
            if total > n:
                break
            if isPrime[total]:
                largest = total

        return largest
