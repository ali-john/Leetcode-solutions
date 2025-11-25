class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        target = sum(nums) // 2

        @cache
        def dp(i,total):
            if total == 0:
                return True
            if i == n:
                return False
            
            if total < 0 or total > target:
                return False
   
            
            if nums[i] <= total:
                if dp(i+1, total - nums[i]):
                    return True
                return dp(i+1, total)
                #take = dp(i+1, total - nums[i])
                # dont_take = dp(i+1, total)
                # ans = take or dont_take
            else:
                ans = dp(i+1, total)
            return ans
        
        if sum(nums) % 2 != 0:
            return False
        else:
            if dp(0, target):
                return True
            else:
                return False
        
                
            

