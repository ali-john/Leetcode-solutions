class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0 

        for num in nums:
            xor^=num
        diff_bit = 1
        while not (diff_bit&xor):
            diff_bit = (diff_bit<<1)
        
        first = 0
        second = 0
        for num in nums:
            if num&diff_bit:
                first^=num
            else:
                second^=num
        return [first,second]

        

        
