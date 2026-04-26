class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        c = Counter(s)
        curr = c['0']
        ans = curr
        for char in s:
            if char == '0':
                curr-=1
                ans = min(ans, curr)
            else:
                curr+=1
        return ans

        
        # ones = [0]*n
        # zeros = [0]*n
        # ones[0] = 1 if s[0] == '1' else 0
        # zeros[0] = 1 if s[0] == '0' else 0
        # for i in range(1, n):
        #     if s[i] == '1':
        #         ones[i] = ones[i-1] + 1
        #         zeros[i] = zeros[i - 1]
        #     else:
        #         zeros[i] = zeros[i - 1] + 1
        #         ones[i] = ones[i-1]

        # ans = float('inf')
        # for i in range(n):
        #     if i - 1 >0 and s[i] == '1':
        #         zero_next = zeros[-1] - zeros[i]
        #         ones_prev = ones[i-1]
        #         ans = min(ans, zero_next+ones_prev)
        #     elif i - 1 > 0 and s[i] == '0':
        #         ones_prev = ones[i - 1]
        #         zeros_next = zeros[-1] - zeros[i]
        #         ans = min(ans, ones_prev + zeros_next)
        # # check first char
        # ans = min(ans, zeros[-1] - zeros[0])
        # return ans

