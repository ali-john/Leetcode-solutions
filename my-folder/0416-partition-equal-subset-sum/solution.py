class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        dp = [[False for _ in range(total+1)] for _ in range(n+1)]
        def recur(nums,n,total):
            for i in range(n+1):
                dp[i][0] = True

            for i in range(1,n+1):
                for j in range(1,total+1):
                    if nums[i-1]>j:
                        dp[i][j] = dp[i-1][j]
                    if nums[i-1]<=total:
                        dp[i][j] = dp[i-1][j - nums[i-1]] or dp[i-1][j]
            return dp[n][total]
        
        if total%2!=0:
            return False
        else:
            return recur(nums,n,total//2)
        

        
