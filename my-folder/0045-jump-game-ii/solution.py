class Solution:
    def jump(self, nums: List[int]) -> int:
        MAX = 1000000009
        n = len(nums)

        @cache
        def dp(i):
            if i>= n-1:
                return 1
            
            total = float('inf')
            loc = 0
            for jump in range(1,nums[i]+1):
                loc = dp(i+jump) + 1
                total = min(loc,total)
            
            return total
        
        return dp(0) - 1

            
            



