class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        left_count = defaultdict()
        right_count = defaultdict()
        
        letters = list(string.ascii_lowercase)

        for letter in letters:
            left_count[letter] = [0]*n
            right_count[letter] = [0]*n
        
        # fill counts
        for i in range(n):
            left_count[s[i]][i]+=1
            right_count[s[i]][i]+=1
        
        # add counts
        for letter in letters:
            for i in range(1, n):
                left_count[letter][i] += left_count[letter][i-1] 
        
        for letter in letters:
            right_sum = sum(right_count[letter])
            for i in range(n):
                right_sum -= right_count[letter][i]
                right_count[letter][i] = right_sum

            
        # print(left_count)
        # print(right_count)
        ans = 0
        for i in range(n):
            lc = 0
            rc = 0
            for letter in letters:
                if left_count[letter][i] > 0:
                    lc+=1
                if right_count[letter][i] > 0:
                    rc+=1
    
            if lc == rc:
                ans+=1
        return ans

                
            
