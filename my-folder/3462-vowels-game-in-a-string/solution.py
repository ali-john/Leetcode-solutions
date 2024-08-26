class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = ['a','e','i','o','u']
        count = 0
        for char in s:
            if char in vowels:
                count+=1
        
        if count==0:
            return False
        else:
            return True


