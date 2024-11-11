class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def sieve(n):
            primes = [True for i in range(n+1)]
            
            p = 2
            while p*p<=n:
                if primes[p]==True:
                    for i in range(p*p,n+1,p):
                        primes[i] = False
                p+=1
        
            prime_num = []
            for i in range(2,n):
                if primes[i]:
                    prime_num.append(i)
            return prime_num
        
        def find_largest_prime(n,primes):
            # return largest primes less than equal to n
            if n<primes[0]:
                return 0
    
            left = 0
            right = len(primes)-1

            while left<=right:
                mid = (left+right)//2
                if primes[mid]<=n:
                    left = mid+1
                else:
                    right = mid-1
            return primes[left-1]
                    
        if len(nums)==1:
            return True
        prev = 0
        primes = sieve(max(nums)+1)
        for num in nums:
            upper_bound = num - prev
            largest_prime = find_largest_prime(upper_bound-1,primes)
            if num - largest_prime <=prev:
                return False
            
            prev = num - largest_prime
        return True


            
                
        
