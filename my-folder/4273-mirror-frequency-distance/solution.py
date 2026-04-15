class Solution:
    def mirrorFrequency(self, s: str) -> int:
        n = len(s)
        solved = set()
        mapping = {'0':'9', '1':'8', '2':'7', '3':'6', '4':'5','5':'4', '6':'3', '7':'2', '8':'1', '9':'0'}
        def get_letter(curr):
            return chr( (ord('z') - ord(curr)) + ord('a') )
        
        table = Counter(s)
        ans = 0
        for char in s:
            if char not in solved:
                if char.isdigit():
                    c = char
                    m = mapping[c]
                    ans+=(abs(table[c] - table[m]))
                    solved.add(c)
                    solved.add(m)
                else:
                    m = get_letter(char)
                    ans+= abs( table[m] - table[char])
                    solved.add(m)
                    solved.add(char)
        return ans

