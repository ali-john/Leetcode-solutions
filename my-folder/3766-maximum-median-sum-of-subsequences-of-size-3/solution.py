class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums, reverse = True)
        ans = 0
        to_get = n // 3
        i = 1
        while to_get:
            ans+=sorted_nums[i]
            i+=2
            to_get-=1
        return ans


