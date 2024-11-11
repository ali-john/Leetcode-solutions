class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digits = [char for char in str(x)]
        s = 0
        for char in digits:
            s+=int(char)

        if x%s==0:
            return s
        else:
            return -1
