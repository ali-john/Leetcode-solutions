class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        n = len(s)
        modulo = 1000000007
        string = [0]*26
        for char in s:
            string[ord(char)-ord("a")]+=1
        

        while t:
            temp = [0]*26
            for i in range(26):
                if i==25:
                    temp[0] = (temp[0]+string[25])%modulo
                    temp[1] = (temp[1]+string[25])%modulo
                else:
                    temp[i+1] = (string[i])%modulo
            string = temp[:]
            t-=1
        return sum(string)%modulo



        
