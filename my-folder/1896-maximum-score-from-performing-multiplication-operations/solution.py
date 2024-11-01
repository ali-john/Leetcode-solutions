class Solution:
    def maximumScore(self, nums: List[int], mul: List[int]) -> int:
        n = len(nums)
        m = len(mul)
        dp = [[-1 for _ in range(m+1)]  for _ in range(m+1)]
        def solve(start,i):
            if i>=len(mul):
                return 0
            if dp[start][i]!=-1:
                return dp[start][i]
            end = (n - (i-start))-1
            
            first = nums[start]*mul[i] + solve(start+1,i+1)
            second = nums[end]*mul[i] + solve(start,i+1)

            ans = max(first,second)
            dp[start][i] = ans
            return ans
        return solve(0,0)
