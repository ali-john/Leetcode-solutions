class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_ans = 0
        n = len(accounts)
        m = len(accounts[0])

        for i in range(n):
            local = 0
            for j in range(m):
                local+=accounts[i][j]
            max_ans = max(max_ans,local)
        return max_ans
