class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        prefix = [[0]*n for _ in range(26)]

        for i,char in enumerate(s):
            index = ord(char) - ord('a')
            prefix[index][i]+=1
        
        for i in range(26):
            for j in range(1,n):
                prefix[i][j] += prefix[i][j-1]

        count = 0
        all_ = set()
        for i in range(n):
            char = s[i]
            index = ord(char) - ord('a')

            if i>1: # check same two chars on left
                if prefix[index][i-1]>=2:
                    palindrome = char*3
                    if palindrome not in all_:
                        count+=1
                        all_.add(palindrome)
            if n - i >2: # check same two chars on right
                if prefix[index][-1] - prefix[index][i] >=2:
                    palindrome = char*3
                    if palindrome not in all_:
                        count+=1
                        all_.add(palindrome)
            if i>0 and i<n-1: # check xax type palindromes
                char_found = []
                for j in range(26):
                    if prefix[j][i-1] >=1 and (prefix[j][-1] - prefix[j][i]) >=1:
                        char_found.append(chr(j + ord('a') ))
                for ch in char_found:
                    palindrome = ch + char + ch
                    if palindrome not in all_:
                        count+=1
                        all_.add(palindrome)
        return count




