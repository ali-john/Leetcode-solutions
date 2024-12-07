class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        
        def sieve(n):
            primes = [True for _ in range(n+1)]
            p =2
            while p*p<=n:

                if primes[p]:
                    for i in range(p*p,n+1,p):
                        primes[i]= False
                p+=1
            output = []
            for i in range(2,n+1):
                if primes[i]:
                    output.append(i)
            return output
        

        primes = Counter(sieve(n))
        ans = []
        added = set()

        for prime,times in primes.items():
            second_num = n - prime
            if second_num in primes and (prime not in added and second_num not in added) :
                ans.append([prime,second_num])
                added.add(prime)
                added.add(second_num)

        return ans

            

