class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result = 0
        for num in nums:
            result^=num
        diff_bit = 1
        while not (result & diff_bit):
            diff_bit = diff_bit<<1
        a, b = 0, 0
        for num in nums:
            if num&diff_bit:
                a ^= num
            else:
                b^=num
        return [a,b]
        

        

        
