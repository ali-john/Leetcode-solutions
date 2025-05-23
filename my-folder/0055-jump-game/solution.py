class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # linear solution
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal ==0 else False
        
        # n = len(nums)

        # @cache
        # def dp(i):
        #     if i>=n-1:
        #         return True
        #     if nums[i] == 0:
        #         return False
            
        #     for jump in range(1, nums[i]+1):
        #         if dp(i+jump):
        #             return True
        #     return False
        
        # return dp(0)

