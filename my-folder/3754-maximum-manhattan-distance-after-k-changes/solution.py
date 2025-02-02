class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        n = len(s)
        x= 0
        y = 0
        max_ans = 0
        for i, c in enumerate(s,1):
            if c=='N': y+=1
            elif c=='S': y-=1
            elif c=='E': x+=1
            elif c=='W': x-=1
        
            curr = abs(x) + abs(y)
            cand = min(curr + 2*k, i)
            if cand>max_ans:
                max_ans = cand
        return max_ans

