class Solution:
    def minOperations(self, nums: list[int]) -> int:
        LIMIT = 10**5 + 100
        n = len(nums)
         
        def generate_primes():
            sieve = [True]*(LIMIT + 1)
            sieve[0] = sieve[1] = False
            for p in range(2, int(LIMIT**0.5)+1):
                if sieve[p]:
                    for i in range(p*p, LIMIT+1, p):
                        sieve[i] = False
            return [p for p, is_prime in enumerate(sieve) if is_prime]
        def is_prime(number):
            return number > 1 and all(number % i != 0 for i in range(2, int(number**0.5) + 1))
             
        primes = generate_primes()
        #print(f'Primes: {primes}')
        ans = 0
        for i in range(n):
            #print(f'Number {nums[i]}')
            if i%2 == 0:
                if not is_prime(nums[i]):
                    index = bisect_right(primes, nums[i])
                    #print(f'Got Index {index} and primes[index] = {primes[index]}')
                    ans+= (primes[index] - nums[i])
            else:
                if is_prime(nums[i]):
                    if nums[i] == 2:
                        ans+=2
                    else:
                        ans+=1
        return ans



