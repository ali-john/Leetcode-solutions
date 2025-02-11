class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        n = len(s)

        prefix,_,suffix  = p.partition("*")
        start_idx = s.find(prefix)
        #print(f'prefix: {prefix}: start_idx: {start_idx}')
        if start_idx==-1:return False

        else:
            extra = s[start_idx+len(prefix):]
            return suffix in extra
            
        

        

