class Solution:
    def maximumTotalSum(self, nums: List[int]) -> int:

        nums.sort(reverse=True)
        prev_height = nums[0]
        total = 0
        total+=prev_height


        for i in range(1,len(nums)):
            max_height = nums[i]

            if prev_height-1<=max_height:
                height_to_assign = prev_height-1
            else:
                height_to_assign = max_height
            

            if height_to_assign<=0:
                return -1
            
            total+=height_to_assign
            prev_height = height_to_assign
        return total

