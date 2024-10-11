class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        left = 0
        right = n-1
        while left<right:
            mid = (left+right)//2
            if nums[mid-1]!=nums[mid] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            if nums[mid]==nums[mid+1]:
                if mid%2==0:
                    left = mid+1
                else:
                    right = mid-1
            else:
                if mid%2==0:
                    right = mid-1
                else:
                    left = mid+1

            
        return nums[left]
            
