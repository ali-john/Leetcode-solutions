class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        if n == 1 or n == 2:
            return nums
        
        ans = [nums[0]]
        for i in range(1,n-1):
            left_largest = True
            right_largest = True
            for j in range(i):
                if nums[j] >= nums[i]:
                    left_largest = False
                    break
            for j in range(i+1, n):
                if nums[j] >= nums[i]:
                    right_largest = False
                    break
            if left_largest or right_largest:
                ans.append(nums[i])
        ans.append(nums[-1])
        return ans


        
