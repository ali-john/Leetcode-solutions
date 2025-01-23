class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = len(nums)

        ans = 0
        for i in range(n):
            start = max(0,i-nums[i])
            local = 0
            for j in range(start,i+1):
                local+=nums[j]
            ans+=local
        return ans

