class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = ['a','e','i','o','u']
        vc = 0
        for string in s:
            if string in vowels:
                vc+=1
        if vc==0:
            return False
        else:
            return True

