class Solution:
    def answerString(self, word: str, f: int) -> str:
        
        n = len(word)
        if f == 1:
            return word

        max_len = n - f + 1
        ans = ""

        for i in range(n):
            ans = max(ans,word[i:i+max_len])
        return ans
