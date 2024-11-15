from typing import List

class Solution:
    def maxTotalReward(self, reward: List[int]) -> int:
        n = len(reward)
        reward = sorted(reward)

        dp = [[-1]*4001 for _ in range(n)]
    
        def solve(current, index):
            if index >= n:
                return current
            if dp[index][current]!=-1:
                return dp[index][current]
                
            not_take = solve(current, index + 1)
            take = 0
            if reward[index]>current:
                take =  solve(current+reward[index], index + 1)
            
            ans = max(take, not_take)
            dp[index][current]  = ans
            return dp[index][current]
        
        return solve(0, 0)  

