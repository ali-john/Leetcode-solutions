class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0

        for i in range(len(nums)):
            ones = ones^nums[i]
            ones = ~(twos)&ones

            twos = twos^nums[i]
            twos = ~(ones)&twos
        return ones
        
        
