class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Understand from here: https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/solutions/8289598/on-check-rotated-increasingdecreasing-or-ybx5
        n = len(nums)
        breaks = 0
        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                breaks+=1
        if breaks == 0: # already sorted
            return 0 
        zero_index = nums.index(0)
        if breaks == 1:
            ans = zero_index
            ans = min(zero_index, 2 + n - ans)
            return ans
        if n - breaks == 1:
            ans = n - zero_index
            ans = min(ans, zero_index + 2)
            return ans
        return -1

