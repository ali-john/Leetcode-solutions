class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(words)
        count = 0

        for word in words:
            if word.startswith(pref):
                count+=1
        return count
