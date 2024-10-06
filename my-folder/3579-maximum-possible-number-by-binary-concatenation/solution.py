class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
    
        output = max(
           int (bin(nums[0])[2:]+ bin(nums[1])[2:] + bin(nums[2])[2:],2),
           int (bin(nums[0])[2:]+ bin(nums[2])[2:] + bin(nums[1])[2:],2),
           int (bin(nums[1])[2:]+ bin(nums[0])[2:] + bin(nums[2])[2:],2),
           int (bin(nums[1])[2:]+ bin(nums[2])[2:] + bin(nums[0])[2:],2),
           int (bin(nums[2])[2:]+ bin(nums[0])[2:] + bin(nums[1])[2:],2),
           int (bin(nums[2])[2:]+ bin(nums[1])[2:] + bin(nums[0])[2:],2)

        )
        
        return output
