class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [-1]*n

        for i in range(n):
            max_num = nums[i]
            for j in range(1,max_num+1):
                if (j| j+1)==max_num:
                    output[i] = j
                    break
        return output
            

