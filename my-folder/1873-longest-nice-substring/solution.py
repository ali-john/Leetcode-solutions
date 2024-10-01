class Solution:
    def longestNiceSubstring(self, s: str) -> str:
    
        
        n = len(s)
        
        max_string = ""
        prev_len = 0
        for i in range(n):
            seen_lower = set()
            seen_upper = set()
            for j in range(i,n):
                if s[j].isupper():
                    seen_upper.add(s[j].lower())
                else:
                    seen_lower.add(s[j])
                is_nice = True
                if not seen_upper==seen_lower:
                    is_nice = False

                if is_nice:
                    if j-i+1>prev_len:
                        max_string = s[i:j+1]
                        prev_len = j-i+1
        return max_string




