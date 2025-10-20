class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        n = len(words)
        if n < 3 : return [0]*n
        
        def find_len(word1, word2):
            l1, l2 = len(word1), len(word2)
            ans = 0
            for i in range(min(l1,l2)):
                if word1[i] == word2[i]:
                    ans+=1
                else:
                    break
            return ans

        prefix = [0]*n
        suffix = [0]*n
        
        # precompute max so far
        maxi = 0
        for i in range(1,n):
            ans = find_len(words[i], words[i-1])
            maxi = max(ans,maxi)
            prefix[i] = maxi
        maxi = 0
        # precompute suffix so far
        for i in range(n-2,-1,-1):
            ans = find_len(words[i], words[i+1])
            maxi = max(ans, maxi)
            suffix[i] = maxi
        
        ans = [0]*n
        for i in range(n):
            
            left_max, right_max , current = 0, 0, 0
            if i - 1 >=0: left_max = prefix[i-1]
            if i + 1 < n: right_max = suffix[i+1]
            if i - 1 >=0 and i + 1 < n:
                current = find_len(words[i-1 ], words[i+1])
            if i == 0:
                right_max = suffix[i+1]
            ans[i] = max(left_max, right_max, current)
        return ans







        
