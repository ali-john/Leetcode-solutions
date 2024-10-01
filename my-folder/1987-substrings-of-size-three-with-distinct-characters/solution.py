class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        if n<3:
            return 0
        total = 0
        win = Counter()
        for i in range(3):
            win[s[i]]+=1
        if len(win)==3:
            total+=1
        left = 0
        for right in range(3,n):
            win[s[right]]+=1
            win[s[left]]-=1

            if win[s[left]]<=0:
                del win[s[left]]
            
            if len(win)==3:
                total+=1
            left+=1

        return total
