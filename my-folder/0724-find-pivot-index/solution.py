class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        prev = 0
        n = len(nums)
        if n==1:
            return 0
        for num in nums:
            prev+=num
            prefix.append(prev)
        for i in range(n):
            if i-1>=0:
                left_sum = prefix[i-1]
            else:
                left_sum = 0
            if i+1<=n:
                right_sum = prefix[-1] - left_sum - nums[i]
            else:
                right_sum=0
            if right_sum==left_sum:
                return i
        return -1
            
