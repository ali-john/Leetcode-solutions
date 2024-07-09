class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        end = 0
        ans = 100000000
        window_sum = 0
        while end<len(nums):
            window_sum += nums[end]

            while window_sum>=target and start<=end:
                ans = min(ans,(end-start)+1)
                window_sum-= nums[start]
                start+=1
            end+=1
        if ans==100000000:
            return 0
        return ans




        
