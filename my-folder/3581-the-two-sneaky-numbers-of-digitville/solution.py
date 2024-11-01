class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        nums = sorted(nums)

        for i,num in enumerate(nums):
            if i+1<n:
                if nums[i]==nums[i+1]:
                    ans.append(num)
        return ans
