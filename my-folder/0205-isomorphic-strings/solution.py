class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        mapper = defaultdict()
        inv_mapper = defaultdict()

        for char1, char2 in zip(s,t):
            if char1 in mapper:
                if mapper[char1]!=char2:
                    return False
            if char2 in inv_mapper:
                if inv_mapper[char2] != char1:
                    return False
            
            mapper[char1] = char2
            inv_mapper[char2] = char1
        return True
