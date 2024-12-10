class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t):
            return False
        s_counter = Counter(s)
        t_counter = Counter(t)

        for key,val in s_counter.items():
            if key not in t_counter:
                return False
        
        ptr = 0
        for i in range(len(s)):
            while ptr<len(t) and t[ptr]!=s[i]:
                ptr+=1
            if ptr>=len(t) and i<len(s):
                return False
            ptr+=1
        return True

        
        
