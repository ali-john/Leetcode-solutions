class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1: return nums[0]

        memo = {}
        # solve assuming you rob house 1
        def solve1(i):
            if i>=n-1: return 0
            if i in memo: return memo[i]
            dont_rob = solve1(i+1)
            rob = nums[i] + solve1(i+2)
            memo[i] = max(dont_rob,rob)
            return memo[i]

        memo2 = {}
        def solve2(i):
            if i>=n: return 0
            if i in memo2: return memo2[i]
            dont_rob = solve2(i+1)
            rob = nums[i] + solve2(i+2)
            memo2[i] = max(rob,dont_rob)
            return memo2[i]

        ans = max(solve1(0), solve2(1) )
        return ans


        

