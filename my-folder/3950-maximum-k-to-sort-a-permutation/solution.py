class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)

        ands = []
        for i in range(n):
            if nums[i] != i:
                ands.append(nums[i])
        if len(ands) > 0:
            ans = ands[0]
            for i in range(1, len(ands)):
                ans&=ands[i]
            return ans
        else:
            return 0

