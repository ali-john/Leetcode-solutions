class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        n = len(arrivals)
        ans = 0

        left = 0
        right = 0
        table = defaultdict(int)
        s = set()
        while right < n:
            table[arrivals[right]]+=1
            while left < right and (right - left + 1) > w:
                if left in s:
                    left+=1
                    continue
                table[arrivals[left]]-=1
                if table[arrivals[left]] == 0: del table[arrivals[left]]
                left+=1
            if table[arrivals[right]] > m:
                ans+=1
                table[arrivals[right]]-=1
                s.add(right)
            right+=1
        return ans




