class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        table = {0:-1}
        n = len(nums)
        count = 0
        prev = 0
        for i in range(n):
            prev+=nums[i]
            if  (prev - target) in table:
                count+=1
                table = {}
            table[prev]=i
        return count

