class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1]*n for _ in range(n)]
        
        def solve(left,right,target):
            if left>=right:
                return 0
            
            if dp[left][right]!=-1:
                return dp[left][right]
            
            ans = 0
            if nums[left]+nums[right]==target:
                ans =  max(ans,1+solve(left+1,right-1,target))
            if nums[left]+nums[left+1]==target:
                ans = max(ans,1+solve(left+2,right,target))
            if nums[right]+nums[right-1]==target:
                ans = max(ans,1+solve(left,right-2,target))
            
            dp[left][right] = ans
            return dp[left][right]
            #return dp[left][right]
        
        opt1 = solve(0,n-1,nums[0]+nums[n-1])
        dp = [[-1]*n for _ in range(n)]
        opt2 = solve(0,n-1,nums[0]+nums[1])
        dp = [[-1]*n for _ in range(n)]
        opt3 = solve(0,n-1,nums[n-1]+nums[n-2])
        return max(opt1,opt2,opt3)
