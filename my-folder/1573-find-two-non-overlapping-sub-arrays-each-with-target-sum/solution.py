class Solution:
    def minSumOfLengths(self, nums: List[int], target: int) -> int:
        # DP with sliding window


        n = len(nums)

        left = 0
        dp = [float('inf')]*n
        running_sum = 0
        min_len = float('inf')
        ans = float('inf')
        for right, num in enumerate(nums):
            running_sum += nums[right]

            while running_sum > target:
                running_sum -= nums[left]
                left+=1
            
            if running_sum == target: 
                current_length = right - left + 1
                if left > 0 and dp[left - 1] != float('inf'):
                    ans = min(ans, dp[left - 1] + current_length)
                
                min_len = min(min_len, current_length)
            dp[right] = min_len
        
        return ans if ans != float('inf') else -1
        
        
        
        


