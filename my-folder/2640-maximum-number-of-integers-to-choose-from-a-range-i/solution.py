class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_hash = Counter(banned)

        ans = []
        total = 0
        for i in range(1,n+1):
            if i not in banned_hash:
                total+=i
                if total>maxSum:
                    return len(ans)
                else:
                    ans.append(i)
        return len(ans)

