class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1]*n
        suffix = [1]*n
        ans = [1]*n

        prefix[0] = nums[0]
        suffix[-1] = nums[-1]

        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i]
        
        for i in range(n-1-1, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]
        

        for i in range(1,n-1):
            ans[i] = prefix[i-1] * suffix[i+1]
        
        ans[0] = suffix[1]
        ans[-1] = prefix[-2]

        return ans
