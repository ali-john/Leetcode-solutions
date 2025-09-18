class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        n = len(nums)
        if n == 0:
            return [[lower, upper]]

        ans = []
        if n and nums[0]!=lower:
            ans.append([lower, nums[0]-1])
        for i in range(1,n):
            if nums[i] - nums[i-1]!=1:
                ans.append([nums[i-1]+1, nums[i] - 1])
        if n and nums[-1]!=upper:
            ans.append([nums[-1]+1, upper])
        return ans

