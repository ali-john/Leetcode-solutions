class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)

        count = Counter(s)

        delete = 0
        for freq in count.values():
            if freq%2==1:
                delete+=freq-1
            else:
                delete+=freq-2
        return n-delete
