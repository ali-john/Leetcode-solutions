class Solution:
    def minimumLevels(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                nums[i] = -1
        total_sum = sum(nums)

        prefix_sum = 0
        ans = -1
        for i in range(n - 1):
            prefix_sum+=nums[i]
            rest = total_sum - prefix_sum
            if prefix_sum > rest:
                ans = i+1
                break
        return ans

