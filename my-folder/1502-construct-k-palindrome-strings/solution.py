class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k: return False
        count  = Counter(s)

        c = 0
        for key,v in count.items():
            if v%2!=0: c+=1
            if c>k: return False
        return True
