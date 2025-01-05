class Solution:
    def calculateScore(self, s: str) -> int:
        
        def mirror(c):
            return chr(219 - ord(c))
        
        mapper = defaultdict(list)
        total = 0
    
        for i, char in enumerate(s):
            mirror_char = mirror(char)
    
            if mapper[mirror_char]:
                j = mapper[mirror_char].pop()
                total += (i - j)
            else:
                mapper[char].append(i)
    
        return total
