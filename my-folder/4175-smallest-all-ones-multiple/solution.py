class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        if k % 2 ==0 or k%5 == 0: return -1

        remainder = 1 % k
        seen = set()
        length = 1

        while remainder != 0:
            if remainder in seen:
                return -1
            
            seen.add(remainder)
            remainder = ( remainder * 10 + 1 ) % k
            length+=1
        return length

