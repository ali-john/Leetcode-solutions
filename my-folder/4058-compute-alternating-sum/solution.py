class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        pos = 0
        neg = 0
        for i in range(n):
            if i%2 == 0:
                pos+=nums[i]
            else:
                neg+=nums[i]
        
        return pos - neg
