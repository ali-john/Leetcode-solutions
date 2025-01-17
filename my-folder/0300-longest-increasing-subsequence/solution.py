class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        LIS = [1]*n

        for i in reversed(range(n)):
            for j in range(i+1,n):
                if nums[j] > nums[i]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)

            

            
