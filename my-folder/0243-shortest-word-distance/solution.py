class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        ptr1 = -1
        ptr2 = -1
        ans = float("inf")

        for i, word in enumerate(wordsDict):
            if word == word1:
                ptr1 = i
            if word == word2:
                ptr2 = i
            
            if ptr1>=0 and ptr2>=0:
                ans = min(ans, abs(ptr1 - ptr2))
                if ans == 1:
                    return ans
        return ans










        # indices_word1 = []
        # indices_word2 = []

        # for i in range(len(wordsDict)):
        #     word = wordsDict[i]
        #     if word == word1:
        #         indices_word1.append(i)
        #     if word == word2:
        #         indices_word2.append(i)
    
        # ans = float('inf')
        # for i in range(len(indices_word1)):
        #     for j in range(len(indices_word2)):
        #         diff = abs(indices_word1[i] - indices_word2[j])
        #         ans = min(ans, diff)
        # return ans



