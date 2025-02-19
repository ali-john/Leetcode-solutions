class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        total = []
        def get(s):
            if len(s) == n:
                total.append(s)
                return 
            
            for char in ['a','b','c']:
                if len(s)>0 and char==s[-1]: continue
                get(s+char)
        get("")
        if len(total)<k: return ""
        else:
            total.sort()
            return total[k-1]
            



