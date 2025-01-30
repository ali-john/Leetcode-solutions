class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        ans = 0
        memo = [[-1]*m for _ in range(n)]
        def dp(i,j):
            if i>=n or j>=m: return 0
            if memo[i][j]!=-1: return memo[i][j]

            dp(i+1,j)
            dp(i,j+1)
            memo[i][j] = dp(i+1,j+1)+1 if nums1[i]==nums2[j] else 0
            nonlocal ans
            ans = max(ans,memo[i][j] )
            return memo[i][j]
        dp(0,0)
        return ans

            
