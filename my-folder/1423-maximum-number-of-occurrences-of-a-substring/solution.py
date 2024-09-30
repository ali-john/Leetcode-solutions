class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)

        freq = defaultdict(int)
        result = defaultdict(int)
        left = 0
        for r in range(n):
            freq[s[r]]+=1

            while (r-left+1)>minSize:
                freq[s[left]]-=1
                if freq[s[left]]<=0:
                    del freq[s[left]]
                left+=1
            
            if (r-left+1)>=minSize and (r-left+1)<=maxSize:
                if len(freq)<=maxLetters:
                    result[s[left:r+1]]+=1
    
        return max(result.values()) if result else 0


