class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        runs = defaultdict(list)
        i = 0
        while i < n:
            j = i
            c = s[i]
            while j < n and s[j] == c:
                j += 1
            runs[c].append(j - i)
            i = j

        ans = -1
        for c, arr in runs.items():
            if sum(arr) < 3:
                continue
            left, right = 1, max(arr)
            while left <= right:
                mid = (left + right) // 2
                total = 0
                for r in arr:
                    if r >= mid:
                        total += (r - mid + 1)
                        if total >= 3:
                            break
                if total >= 3:
                    ans = max(ans, mid)
                    left = mid + 1
                else:
                    right = mid - 1
        return ans
        
