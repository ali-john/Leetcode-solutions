class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def solve(rem):
            if rem==0:
                return 1
            if rem<0:
                return 0
            
            return solve(rem-1)+ solve(rem-2)
        return solve(n)
