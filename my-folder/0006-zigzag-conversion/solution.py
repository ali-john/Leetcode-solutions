class Solution:
    def convert(self, s: str, n: int) -> str:
        if n==1 or n>=len(s):
            return s
        rows = [[] for _ in range(n)]
        index,direction = 0,1
        for char in s:
            rows[index].append(char)
            if index==0:
                direction= 1
            elif index==n-1:
                direction = -1
            
            index+=direction
        
        for i in range(n):
            rows[i] = ''.join(rows[i])
        
        return ''.join(rows)
                
