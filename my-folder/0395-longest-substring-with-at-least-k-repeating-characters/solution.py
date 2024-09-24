class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        freq = Counter(s)

        if n<k:
            return 0 
        
        if all(freq[char]>=k for char in freq):
            return n
        
        max_len = 0
        start = 0

        for i, char in enumerate(s):
            if freq[char]<k:
                max_len = max(max_len,self.longestSubstring(s[start:i],k))
                start = i+1
        max_len = max(max_len,self.longestSubstring(s[start:],k))

        return max_len




            

            

            
            

            
            




