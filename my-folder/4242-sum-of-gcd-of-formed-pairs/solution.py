class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefix = []
        max_ = float('-inf')
        for num in nums:
            max_ = max(max_, num)
            prefix.append(gcd(max_, num))
        prefix = sorted(prefix)
        n = len(prefix)
        ans = 0
        for i in range(n//2):
            ans+=gcd(prefix[i], prefix[n- i - 1])
        return ans
