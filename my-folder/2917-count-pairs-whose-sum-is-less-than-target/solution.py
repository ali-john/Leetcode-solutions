class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:

        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] < target:
        #             count+=1
        # return count
        count = 0
        nums.sort()
        l = 0
        h = len(nums) - 1

        while l < h:
            if nums[l] + nums[h] < target:
                count+=(h-l)
                l+=1
            else:
                h-=1
        return count
