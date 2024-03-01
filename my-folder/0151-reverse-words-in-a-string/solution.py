class Solution:
    def reverseWords(self, s: str) -> str:
        res = s.split()
        res = res[::-1]
        output = ' '.join(res)
        return output
        

