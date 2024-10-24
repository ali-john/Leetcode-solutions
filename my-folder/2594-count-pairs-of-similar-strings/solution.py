class Solution:
    def similarPairs(self, words: List[str]) -> int:
        n = len(words)
        local = 0
        for i in range(n):
            for j in range(i+1,n):
                word1 = Counter(words[i])
                word2 = Counter(words[j])
                if word1.keys()==word2.keys():
                    local+=1

        return local
            



