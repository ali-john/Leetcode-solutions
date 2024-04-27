class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        out = dict()
        s_list = s.split()
        if len(s_list)!= len(pattern):
            return False

        for i in range(len(pattern)):
            a = pattern[i]
            b = s_list[i]
            if a in out:
                val = out[a]
                if val != b:
                    return False
            else:
                if b in out.values():
                    return False
                else:
                    out[a] = b
        return True
        
