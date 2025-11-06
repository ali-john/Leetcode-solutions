class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 0:
            if n > 0: return nums[0]
            else: return -1
        if k == 1:
            if n > 1:
                return nums[1]
            elif n == 1: return -1
        if n == 1:
            if k %2 == 0: return nums[0]
            else: return -1
        ans = -1

        for i in range(n):
            ops = i - 0 + 2
            if ops <= k:
                ans = max(ans, nums[i])
        if ans!=-1:
            if k < n:
                ans = max(ans, nums[k])
        return ans
        
