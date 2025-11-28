class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        l = len(nums)
        nums.sort()
        res = 0
        curr = 0
        i = 0
        while curr < n:
            if i < l and nums[i] <= curr + 1:
                curr+=nums[i]
                i+=1
            else:
                res+=1
                curr+= curr+1
        return res
