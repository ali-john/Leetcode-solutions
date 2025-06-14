class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        if n <=k and m<=k:
            return 0

        cost = 0
        while n > k:
            n = n - k
            cost+= (k*n)

        while m > k:
            m = m - k
            cost+= (k*m)

        return cost
        
