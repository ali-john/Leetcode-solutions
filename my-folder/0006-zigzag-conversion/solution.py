class Solution:
    def convert(self, s: str, r: int) -> str:
        n =len(s)

        if r == 1:
            return s
        hold = [[] for _ in range(r)]

        setter = 0

        direction = 1
        for i in range(n):

            if setter <= 0:
                direction = 1
                setter = 0
            elif setter == r - 1:
                direction = -1
                
            
            hold[setter].append(s[i])
            setter+= direction
        
        
        ans = ''
        for i in range(r):
            row = ''.join(hold[i])
            ans+=row
        
        return ans
        

            

            




