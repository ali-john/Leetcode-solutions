class Solution:
# 10 = 2 * 5
        # In a Factorial of number "x" , Number of 2's will be greater than Number of 5's
        # So, Count of 5's determines, number of Trailing zeroes in a Factorial
        # Q) How to find number of 5's in "x" factorial ?
        # A) Count Number of 5's from 1 to x 
        # x / 5 --> Gives Number of 5 factors until x
        # x / 25 --> Gives Number of 25 factors until x
        # We also have to check for 5^3, 5^4 as they also have extra 5's in them
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count

        
