class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction = sorted(satisfaction)

        @cache
        def dp(i, time):
            if i >= n:
                return 0
            c1 = satisfaction[i]* time + dp(i+1, time+1)
            c2 = dp(i+1, time)
            ans = max(c1, c2)
            return ans
        return dp(0, 1)
