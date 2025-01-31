class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = defaultdict(int)
        n = len(s)
        left = 0
        right = 0

        ans = 0
        while right<n:
            table[s[right]]+=1

            while left<=right and table[s[right]]>1:
                table[s[left]]-=1
                if table[s[left]]==0:
                    del table[s[left]]
                left+=1
            ans = max(ans,(right-left+1))
            right+=1
        return ans
