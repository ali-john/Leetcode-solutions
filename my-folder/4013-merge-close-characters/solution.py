class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        s = list(s)
        i = 0

        while i < len(s):
            curr = s[i]
            for j in range(i+1, min(i+k+1, len(s))):
                if s[j] == curr:
                    s.pop(j)
                    i= -1
                    break
            i+=1
        return ''.join(s)
        

