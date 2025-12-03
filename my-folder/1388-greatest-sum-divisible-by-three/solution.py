class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        MIN = -100000000

        @cache
        def dp(i, rem):
            if i == n:
                if rem==0:
                    return 0
                else:
                    return MIN
            
            not_take = dp(i+1, rem)
            take = nums[i] + dp(i+1, (rem + nums[i])%3  )
            return max(take, not_take)
        
            
        return dp(0, 0)
