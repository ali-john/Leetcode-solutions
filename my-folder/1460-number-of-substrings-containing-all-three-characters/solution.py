class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)

        left = 0
        ans = 0
        map = defaultdict(int)
        for right in range(n):
            map[s[right]]+=1

            while len(map)==3:
                ans+=(n-right)
                map[s[left]]-=1
                if map[s[left]]==0:
                    del map[s[left]]
                left+=1
    
        return ans
