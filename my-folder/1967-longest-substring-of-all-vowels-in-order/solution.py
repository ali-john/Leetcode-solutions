class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        n = len(word)

        max_count = left =  0
        s = set()
        max_ord = ord(word[0])
        for right in range(n):
            s.add(word[right])


            if ord(word[right])>= max_ord:
                max_ord = ord(word[right])
            else:
                s = set()
                left = right
                max_ord = ord(word[right])
                s.add(word[right])

            if len(s)==5:
                max_count = max(max_count, (right-left+1))

        return max_count






        
