class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        large = int( ceil( n / 2) )
        nums = [abs(num)**2 for num in nums]
        nums.sort(reverse = True)
        ans = 0
        for i in range(n):
            if i < large:
                ans+=nums[i]
            else:
                ans-=nums[i]
        return ans
