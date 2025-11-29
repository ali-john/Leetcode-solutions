class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dp(i,takeEven):
            if i >=n: return 0

            take = 0
            dont_take = dp(i+1, takeEven)

            if takeEven:
                take = nums[i] + dp(i+1, False)
            else:
                take = -nums[i] + dp(i+1, True)
            
            ans = max(take, dont_take)
            return ans
        ans = dp(0, True)
        return ans


