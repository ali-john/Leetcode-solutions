class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        total_zeros = nums.count(0)
        ans = 0
        for i in range(n - 1, n  - total_zeros -1, -1):
            num = nums[i]
            if num!=0:
                ans+=1
        return ans
