class Solution:
    def minimumFlips(self, n: int) -> int:
        binary = bin(n)[2:]
        reversed_bin = binary[::-1]

        ans = 0
        for b1,b2 in zip(binary, reversed_bin):
            if b1!=b2:
                ans+=1
        return ans

