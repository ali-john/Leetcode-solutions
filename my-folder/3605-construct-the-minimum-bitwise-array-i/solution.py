class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [-1]*n

        def find_num(num):

            for i in range(1,num):
                if i | (i+1)==num:
                    return i
            return -1

        for i in range(n):
            output[i] = find_num(nums[i])
        return output
            
        
            

