class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        #res = math.exp(math.log(x)/2)
        #print(res)
        #res = int(ceil(res))
        res = x**0.5
        return int(res)
        
