class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n-1):
            left_sum = sum(nums[0:i+1])
            right_sum = sum(nums[i+1:])
            diff = left_sum - right_sum
            if diff%2==0: ans+=1
            
        return ans
