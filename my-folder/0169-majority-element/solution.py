class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            
            if candidate == num:
                count+=1
            else:
                count-=1
        return candidate
