class Solution:
    def passwordStrength(self, password: str) -> int:
        p = set(password)
        # print(p)
        ans = 0
        for char in p:
            if char in ["!","#","@","$"]:
                ans+=5
            elif char.isdigit():
                ans+=3
            elif char.isupper():
                ans+=2
            else:
                ans+=1
        return ans
