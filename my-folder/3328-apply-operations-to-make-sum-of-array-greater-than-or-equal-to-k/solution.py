class Solution:
    def minOperations(self, k: int) -> int:


        if k==1:
            return 0

        op = float('inf')

        for a in range(1,k):
            b = (math.ceil(k/(a))) - 1
            op = min(op,(a+b-1))
        return op
        
                
            
