class Solution:
    def maxJump(self, nums: List[int]) -> int:
        
        max_jump = 0
        even_prev = nums[0]
        odd_prev = nums[1]
        for i in range(len(nums)):
            if not i%2: # if odd
                max_jump = max(max_jump,abs(nums[i]-odd_prev))
                odd_prev = nums[i]
            else:
                max_jump = max(max_jump,abs(nums[i]-even_prev))
                even_prev = nums[i]
        return max_jump
        


