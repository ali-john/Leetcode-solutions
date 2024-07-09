class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        window_start = 0
        window_end = 0
        output = float("-inf")
        hash_table = {}
        maxRepeatedCount = 0
        while window_end<len(s):
            endChr = s[window_end]
            hash_table[endChr] = hash_table.setdefault(endChr,0)+1
            maxRepeatedCount = max(maxRepeatedCount,hash_table[endChr])

            if (window_end - window_start+1 - maxRepeatedCount > k):
                startChr = s[window_start]
                hash_table[startChr]-=1
                window_start+=1
            
            output = max(output,(window_end-window_start)+1)
            window_end+=1
        return output


















        
