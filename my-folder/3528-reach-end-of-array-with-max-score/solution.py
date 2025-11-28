class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:

        n = len(nums)
        idx = 0
        l = nums[0]
        ans = 0

        for i in range(1, n):
            if nums[i] > l:
                k = i - idx
                ans+= (l*k)
                l = nums[i]
                idx = i
        k = n - 1 -idx
        ans+=(l*k)
        return ans

            


