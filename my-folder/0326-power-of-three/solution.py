class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <=0:
            return False
        else:
            tolerance = 0.000000000001
            res = math.log(n,3)
            r = round(res,1)
            if abs(r - res)<=tolerance:
                return True
            else:
                return False
