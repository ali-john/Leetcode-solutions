class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 2:
            return 1

        right = [0]*n
        right[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            right[i] = min(nums[i], right[i+1])
        
        left_max = nums[0]
        ans = -1
        for i in range(n-1):
            left_max = max(left_max, nums[i])
            if left_max <= right[i+1]:
                ans = i+1
                break
        return ans
                



        
