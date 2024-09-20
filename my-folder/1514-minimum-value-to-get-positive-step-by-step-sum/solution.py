class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0]*n
        ans = 1
        prev = 0
        for num in nums:
            prev+=num
            ans = min(ans,prev)
        if ans>0:
            return ans
        else:
            return (-1*ans)+1
        

