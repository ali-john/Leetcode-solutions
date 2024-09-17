class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(shifts)
        prefix = [0]*n
        prev = 0
        for i in range(n-1,-1,-1):
            prev += shifts[i]
            prefix[i] = prev
        output = ""
        for i in range(n):
            calc = ((ord(s[i])+prefix[i]) - ord('a'))%26 + ord('a')
            new_char = chr(calc)
            output+= new_char
            
        return output
            

