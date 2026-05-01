class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        counter = [0]*26
        for c1,c2 in zip(s,t):
            diff = (ord(c2) - ord(c1)) % 26
            if diff > 0 and counter[diff]*26 + diff > k:
                return False
            counter[diff]+=1
        return True
