class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_l = list(s.split(" "))
        p_l = [char for char in pattern]

        if len(s_l)!=len(p_l): return False

        mapper = defaultdict()
        inv_mapper = defaultdict()

        for char1, word1 in zip(p_l,s_l):
            if char1 in mapper:
                if mapper[char1] != word1:
                    return False
            
            if word1 in inv_mapper:
                if inv_mapper[word1]!=char1:
                    return False
            
            mapper[char1] = word1
            inv_mapper[word1] = char1
        
        return True
