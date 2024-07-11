class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # two pointers approach
        right = 1
        left = 1

        while right<len(nums):
            if nums[right]!=nums[left-1]:
                nums[left] = nums[right]
                left+=1
            right+=1
        return left
         


        
