class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        table = defaultdict(int)

        ans = 0
        right = 0
        
        while right < n:
            table[s[right]]+=1

            while not self.is_valid(table):
                table[s[left]] -= 1
                if table[s[left]] == 0:
                    del table[s[left]]
                left += 1
            ans = max(ans,right-left+1)
            right+=1

        return ans
            

    
    
    
    
    
    
    
    def is_valid(self,map):
        vals = map.values()
        for val in vals:
            if val>2:
                return False
        return True
            
       
                
            
            
