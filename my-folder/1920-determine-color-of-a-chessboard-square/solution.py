class Solution:
    def squareIsWhite(self, c: str) -> bool:
        return (ord(c[0])-ord('a')+int(c[1]))%2==0
