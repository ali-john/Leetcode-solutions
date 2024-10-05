class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        table = Counter(s)
        if k==0:
            return 0
        if table['a']<k or table['b']<k or table['c']<k:
            return -1

        left = 0
        max_window = 0
        

        for right in range(n):
            table[s[right]]-=1

            while table['a']<k or table['b']<k or table['c']<k and left<=right:
                table[s[left]]+=1
                left+=1
            max_window = max(max_window, (right-left+1))
            
        return n - max_window


