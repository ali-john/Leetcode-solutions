class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 1000000007
        n = len(complexity)
        for i in range(1, n):
            if complexity[i] <= complexity[0]: return 0
        fact = 1
        for i in range(1,n):
            fact = ( fact * i )% MOD
        return fact
        












        
        
        
        
        
        
        
        
        
        
        # MOD = 1000000007
        # n = len(complexity)

        # for i in range(1, n):
        #     if complexity[i] <= complexity[0]:
        #         return 0
        
        # fact = 1
        # for i in range(1,n):
        #     fact = (fact * i)%MOD
        # return fact%MOD
