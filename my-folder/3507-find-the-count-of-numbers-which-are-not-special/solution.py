import math
class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def get_primes(n):
            primes = [True]*(n+1)
            for i in range(2,int(math.sqrt(n))+1):
                if primes[i]==True:
                    for j in range(i*i, n+1, i):
                        primes[j]=False
            prime_nums = [p for p in range(2,n+1) if primes[p]]
            return prime_nums
        
        max_limit = int(r**0.5)+1
        primes = get_primes(max_limit)
    
        special_count = 0
        for p in primes:
            special_number = p * p
            if special_number > r:
                break
            if special_number >= l:
                special_count += 1

        total_numbers = r - l + 1
        non_special_count = total_numbers - special_count
        return non_special_count


        

        



                

        
