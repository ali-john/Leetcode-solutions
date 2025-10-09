class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def solve(i,exp):
            if i>=n: return 0

            if i == n-1:
                count = 0
                if exp + nums[i] == target: count+=1
                if exp - nums[i] == target: count+=1
                return count
            
            positive = solve(i+1, exp + nums[i])
            negative = solve(i+1, exp - nums[i])
            return positive + negative

        return solve(0,0)




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # n = len(nums)
        # memo = {}
        
        # def dp(i,exp):
        #     if i>=n: return 0
        #     if i==n-1:
        #         count = 0
        #         if exp + nums[i] == target: count+=1
        #         if exp - nums[i] == target: count+=1
        #         return count
            
        #     if (i,exp) in memo: return memo[(i,exp)]
        #     positive = dp(i+1,exp + nums[i])
        #     negative = dp(i+1,exp - nums[i])
        #     memo[(i,exp)] = positive + negative
        #     return memo[(i,exp)]
        # return dp(0,0)
        


        


