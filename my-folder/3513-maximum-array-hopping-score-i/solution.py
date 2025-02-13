class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)

        # @cache
        # def dp(i):
        #     if i>=n: return 0
        #     ans = 0
        #     for j in range(i+1,n):
        #         take = dp(j) + nums[j] * (j-i)
        #         ans = max(ans,take)
        #     return ans
        # return dp(0)

        dp = [0]*n
        
        for i in range(n-1):
            for j in range(i+1,n):
                dp[j] = max(dp[j],dp[i] + nums[j]*(j-i))
        return dp[-1]






