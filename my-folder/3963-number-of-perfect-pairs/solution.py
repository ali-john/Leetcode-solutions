class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(key = lambda x: abs(x))

        ans = 0
        end = 1
        for start in range(n):
            while end < n and abs(nums[end]) <= 2*abs(nums[start]):
                end+=1
            ans+= (end - start - 1)
        return ans
