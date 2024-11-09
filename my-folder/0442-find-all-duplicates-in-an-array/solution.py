class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)

        for i in range(n):
            val = abs(nums[i])
            if nums[val-1]<0:
                ans.append(val)
            else:
                nums[val-1]*=-1
        return ans

            

