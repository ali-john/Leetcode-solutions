class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)

        prefix = [0]*n
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] + nums[i]
        
        incr = [True]*n
        for i in range(1,n):
            incr[i] = incr[i-1] and (nums[i-1] < nums[i])
        decr = [True]*n
        for i in range(n-2, -1 , -1):
            decr[i] = decr[i+1] and (nums[i] > nums[i+1])
        
        ans = float('inf')
        valid = False
        
        # try all split points
        for i in range(n - 1):
            if incr[i] and decr[i + 1]:
                valid = True
                left_sum = prefix[i]
                right_sum = prefix[-1] - prefix[i]
                ans = min(ans, abs(left_sum - right_sum))
        
        return ans if valid else -1

        
