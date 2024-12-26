class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        
        @cache
        def solve(index,expression):
            
            if index>=n: return 0
            if index==n-1:
                expression1 = expression + nums[index]
                expression2 = expression - nums[index]
                if expression1==target and expression2==target:
                    return 2
                elif expression1==target or expression2==target: return 1
                else: return 0
            negatives = solve(index+1,expression - nums[index])
            positives = solve(index+1,expression + nums[index])
            return positives+negatives
        
        return solve(0,0)



