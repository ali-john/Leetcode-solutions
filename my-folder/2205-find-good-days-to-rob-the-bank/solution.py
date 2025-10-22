class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        if time == 0:
            return list(range(n))
        if n == 0:
            return []

        left = [0] * n
        for i in range(1, n):
            if security[i] <= security[i-1]:
                left[i] = left[i-1] + 1
            else:
                left[i] = 0

        right = [0] * n
        for i in range(n-2, -1, -1):
            if security[i] <= security[i+1]:
                right[i] = right[i+1] + 1
            else:
                right[i] = 0
        print(left)
        print(right)
        ans = []
        for i in range(time, n - time):
            if left[i] >= time and right[i] >= time:
                ans.append(i)

        return ans
        
