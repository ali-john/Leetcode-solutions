class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift =0 
        while left!=right:
            left = left>>1
            right= right>>1
            shift+=1
        return right<<shift
        

        
