
class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n = len(nums)
        
        @cache
        def solve(i,op1,op2):
            if i==n:
                return 0
            
            ans = nums[i] + solve(i+1,op1,op2) # no operation applied
            if op1: ans = min(ans, (nums[i]+1)//2 + solve(i+1,op1-1,op2) ) # operation1
            if op2 and nums[i]>=k: ans = min(ans, nums[i]-k + solve(i+1,op1,op2-1))# operation2
            if op1 and op2 and (nums[i]+1)//2>=k:  ans = min(ans, (nums[i]+1)//2-k + solve(i+1,op1-1,op2-1)) # operation 1 followed by operation 2
            if op1 and op2 and nums[i]>=k:  ans= min(ans, (nums[i]-k+1)//2 + solve(i+1,op1-1,op2-1)) # operation 2 followed by operation 1
            return ans
            

        return solve(0, op1, op2)

