class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)

        while k:
            min_index = 0
            min_val = nums[0]
            for i in range(1,n):
                if nums[i]<min_val:
                    min_val = nums[i]
                    min_index = i
            
            nums[min_index] = min_val*multiplier
            k-=1
        return nums
