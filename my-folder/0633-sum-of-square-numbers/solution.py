class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        a = 0
        while a<=(c**0.5):
            b = int((c-(a**2))**0.5)
            if (a**2 + b**2)==c:
                return True
            a+=1
        return False

