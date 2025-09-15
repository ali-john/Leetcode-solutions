class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:

        def check_len(string):
            if len(string)%2 == 0:
                return string[:len(string)//2:1] == string[-1:len(string)//2-1: -1]
            
            else:
                return string[:len(string)//2:1] == string[-1:len(string)//2:-1]
        
        
        # check every possibility:
        max_len = float("-inf")
        if check_len(s):
            max_len = max(len(s), max_len)
        if check_len(t):
            max_len = max(len(t), max_len)
        
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                s1 = s[i:j]
                for k in range(len(t)):
                    for l in range(k,len(t)+1):
                        s2 = t[k:l]
                        combined = s1 + s2
                        if check_len(combined):
                            max_len = max(max_len, len(combined))
        return max_len
        
