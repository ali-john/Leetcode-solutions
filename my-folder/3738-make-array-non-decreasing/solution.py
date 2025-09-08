class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        n = len(nums)
        stack = [nums[0]]
        max_v = nums[0]


        for i in range(1, n):
            if nums[i] >= max_v:
                stack.append(max_v)
                max_v = nums[i]
            else:
                continue
        return len(stack)


