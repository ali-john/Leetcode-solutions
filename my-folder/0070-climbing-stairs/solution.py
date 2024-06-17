class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        F = [0]*n
        l = len(F)
        F[0] = 1
        F[1] = 2
        for i in range(2,n):
            F[i] = F[i-2]+F[i-1]
        return F[l-1]
