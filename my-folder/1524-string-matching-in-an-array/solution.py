class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        output = set()
        for i in range(n):
            for j in range(n):
                if i!=j:
                    if words[i] in words[j]:
                        output.add(words[i])
        return list(output)


