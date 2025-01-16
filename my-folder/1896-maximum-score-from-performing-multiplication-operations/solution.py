class Solution:
    def maximumScore(self, nums: List[int], mul: List[int]) -> int:
        n = len(nums)
        m = len(mul)
        dp = [[-1 for _ in range(m+1)] for _ in range(n+1) ]

        def solve(start,i):
            if i>=m:return 0

            if dp[start][i]!=-1: return dp[start][i]
            end = (n - (i-start)) - 1
            from_start = nums[start]*mul[i] + solve(start+1,i+1)
            from_end = nums[end]*mul[i] + solve(start,i+1)
            dp[start][i] = max(from_start,from_end)
            return dp[start][i]
        return solve(0,0)
        
