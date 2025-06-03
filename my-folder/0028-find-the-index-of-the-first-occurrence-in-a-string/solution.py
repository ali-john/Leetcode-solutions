class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)

        if n < m:
            return -1
        
        RADIX = 26
        MOD = 1_000_000_033
        MAX_WEIGHT = 1

        MAX_WEIGHT = pow(RADIX, m - 1, MOD)

        def hash_value(string):
            ans = 0
            factor = 1

            for i in range(m-1, -1, -1):
                ans = (ans + (ord(string[i]) - ord('a')) * factor) % MOD
                factor = (factor*RADIX) % MOD
            return ans%MOD
        
        hash_needle = hash_value(needle)
        hash_hay = hash_value(haystack[:m]) # hash of haystack for first m characters

        for window_start in range(n - m +1):
            if hash_needle == hash_hay:
                if haystack[window_start:window_start+m] == needle:
                    return window_start

            
            if window_start < n - m:
                left_char = ord(haystack[window_start]) - ord("a")
                right_char = ord(haystack[window_start+m]) - ord('a')
                hash_hay = ((hash_hay - left_char * MAX_WEIGHT) * RADIX + right_char) % MOD
                
        
        return -1 

            


