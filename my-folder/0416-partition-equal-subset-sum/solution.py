class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        dp = [[-1 for _ in range(total+1)] for _ in range(n+1)]
        def recur(nums,n,total):
            if total==0:
                return True
            if n==0:
                return False
            
            if dp[n][total]!=-1:
                return dp[n][total]
            
            if nums[n-1]>total:
                dp[n][total] = recur(nums,n-1,total)
            else:
                dp[n][total] = (recur(nums,n-1,total-nums[n-1])) or (recur(nums,n-1,total))
            return dp[n][total]
            

        if total%2!=0:
            return False
        else:
            return recur(nums,n,total//2)
        

        
