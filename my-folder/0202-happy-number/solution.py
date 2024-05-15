class Solution:
    def isHappy(self, n: int) -> bool:
        squares = []
        output = True

        while True:
            digits = [int(d) for d in str(n)]
            s=0
            for i in range(len(digits)):
                s = s+ (digits[i] ** 2)
            n = s
            if sum(digits)==1:
                break
            if s in squares: # pattern repeats
                output = False
                break
            squares.append(s)
        
        return output

        




        
