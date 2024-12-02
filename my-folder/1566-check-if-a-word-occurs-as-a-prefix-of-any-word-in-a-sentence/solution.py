class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        n = len(words)

        ans = -1
        for i in range(n):
            word = words[i]
            if len(word)<len(searchWord):
                continue
            
            else:
                l = r = 0
                is_prefix = True
                while r<len(searchWord):
                    if word[l]==searchWord[r]:
                        l+=1
                        r+=1
                    else:
                        is_prefix = False
                        break
                if is_prefix:
                    ans = i+1
                    return ans
        
        return ans
