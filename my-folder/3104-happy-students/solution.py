class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        res = int(nums[0]!=0)
        nums.append(float('inf'))
        for i in range(len(nums)-1):
            if nums[i]<i+1<nums[i+1]:
                res+=1
        return res
