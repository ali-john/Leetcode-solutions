class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        diff = [abs(ord(s[i])-ord(t[i])) for i in range(n)]
        print(diff)
        max_len = 0
        windowStart = 0
        windowEnd = 0
        current_cost = 0
        for windowEnd in range(n): 
            current_cost += diff[windowEnd]
            
            while current_cost>maxCost:
                current_cost-=diff[windowStart]
                windowStart+=1

            max_len= max(max_len,(windowEnd-windowStart)+1)
        
        return max_len



        
        
        
