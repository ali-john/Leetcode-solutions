class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_bin = bin(x)[2:]
        y_bin = bin(y)[2:]

        max_len = max(len(x_bin),len(y_bin))

        x_bin = x_bin.zfill(max_len)
        y_bin = y_bin.zfill(max_len)

        ans = 0
        for i in range(len(x_bin)):
            if x_bin[i]!=y_bin[i]:
                ans+=1
        return ans

