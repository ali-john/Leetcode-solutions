class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        counter1 = Counter(s1)
        counter2 = Counter(s2)
        if counter1!=counter2: return False
        i = 0
        count = 0
        while i<len(s1):
            if s1[i]!=s2[i]:
                count+=1
            if count>2: return False
            i+=1
        return True

