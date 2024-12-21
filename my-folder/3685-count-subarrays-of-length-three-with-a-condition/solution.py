class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)

        for i in range(n-2):
            first = nums[i]

            if i+1<n and i+2 < n:
                second = nums[i+1]
                third = nums[i+2]
            if (first + third) == (second/2):
                count+=1
        return count


