class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        table = defaultdict()
        for char in message:
            if char in table:
                table[char]+=1
            else:
                table[char]=1
        
        count=0
        for char in bannedWords:
            if char in table:
                if table[char]>=2:
                    return True
                count+=1
                if count>=2:
                    return True
                table[char]-=1
                if table[char]<=0:
                    del table[char]
        return False

