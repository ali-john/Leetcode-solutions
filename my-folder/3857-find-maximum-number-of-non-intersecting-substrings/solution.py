class Solution:
    def maxSubstrings(self, word: str) -> int:
        n = len(word)
        ans = 0

        table = defaultdict(int)
        for i in range(n):
            if word[i] in table:
                prev = table[word[i]]
                if ( i - prev + 1 ) >= 4:
                    ans+=1
                    table = defaultdict(int)
            else:
                table[word[i]] = i
        return ans
            
        



        

