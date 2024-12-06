class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        n = len(words)
        table = defaultdict(list)
        
        for i,word in enumerate(words):
            even, odd = "",""
            for index,char in enumerate(word):
                if index%2==0:
                    even+=char
                else:
                    odd+=char

            even = sorted(even)
            odd = sorted(odd)

            final = "".join(even+odd)
            table[final].append(word)
        return len(table.keys())

            


