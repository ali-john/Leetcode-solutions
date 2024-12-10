class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        max_len = -1
        for length in range(1,n+1):
            freq = defaultdict(int)

            for i in range(n-length+1):
                sub = s[i:i+length]

                if all(c==sub[0] for c in sub):
                    freq[sub]+=1
                    if freq[sub]>=3:
                        max_len = max(max_len,length)
        return max_len
        

