class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = len(s)
        n_spaces = len(spaces)
        new_string = []
        j = 0
        for i in range(n):
            if j<n_spaces and i==spaces[j]:
                new_string.append(' ')
                j+=1
                new_string.append(s[i])
            else:
                new_string.append(s[i])
        return ''.join(new_string)

