class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        right = 1
        prev = nums[0]

        while right<len(nums):
            while right<len(nums) and nums[right]==prev:
                right+=1
            if right<len(nums):
                temp = nums[left]
                nums[left] = nums[right]
                nums[right]=temp
                prev = nums[left]
                left+=1
                right+=1
        return left
            
