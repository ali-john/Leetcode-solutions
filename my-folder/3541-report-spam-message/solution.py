class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        table = Counter(bannedWords)
        ans = 0
        for word in message:
            if word in table:
                ans+=1
        
        return True if ans >=2 else False
