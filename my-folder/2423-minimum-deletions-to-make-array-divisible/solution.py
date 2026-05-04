class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        n = len(numsDivide)
        g = 0
        for num in numsDivide:
            g = gcd(num,g)
        nums = sorted(nums)
        for i in range(len(nums)):

            if g % nums[i] == 0:
                return i
        return -1



