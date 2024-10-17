class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n = len(t)
        ptr = 0
        idx = -10 
        res = 0
        # iterate the length of t
        for i in range(n):
            char = t[i]
            while ptr<len(s):
                if s[ptr]==char:
                    break
                ptr+=1
            # if we have completely iterated s, we need no more iterations, just add remaining t to s
            if ptr>=len(s):
                idx = i -1 
                break
            ptr+=1
        if idx==-10: #nothing to add (t is already a substring of s)
            return 0
        else:
            res = n - idx - 1
            return res

