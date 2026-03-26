class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)
        positives = [num for num in nums if num > 0]
        negatives = [num for num in nums if num < 0] 
        ans = 1
        
        if len(negatives)%2 !=0:
            negatives.sort()
            negatives.pop()
        if not negatives and not positives:
            return max(nums)
        
        for num in positives:
            ans*=num
        for num in negatives:
            ans*=num
        return ans
