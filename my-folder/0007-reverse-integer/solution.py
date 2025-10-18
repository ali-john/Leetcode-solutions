class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX =  -2**31, 2**31 - 1

        digits_x = [ d for d in str(abs(x)) ] 
        reversed_x = int( "".join(reversed(digits_x) ))
        if x < 0:
            reversed_x *=-1
            
        if reversed_x > MAX or reversed_x < MIN: return 0
        return reversed_x

