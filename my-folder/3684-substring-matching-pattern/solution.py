class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        n = len(s)
        prefix, _, suffix = p.partition("*")
        index = s.find(prefix)
        if index == -1: return False
        else:
            extra = s[index+len(prefix): ]
            return suffix in extra
            
