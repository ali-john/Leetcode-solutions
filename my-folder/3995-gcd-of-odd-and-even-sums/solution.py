class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:

        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b, a%b)
        
        odds = [num for num in range(1,2010,2)]
        even = [num for num in range(2,2020,2)]
        oddSum = sum(odds[:n])
        evenSum = sum(even[:n])
        return gcd(oddSum, evenSum)
