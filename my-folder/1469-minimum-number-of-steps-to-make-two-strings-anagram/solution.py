class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)
        ans =0 

        extra = 0
        for char,value in t_count.items():
            if char in s_count:
                s_time = s_count[char]
                if s_time<value:
                    extra+=value - s_time
                    ans+=value - s_time
                elif s_time>value:
                    if s_time-value<=extra:
                        extra-=(s_time-value)       
            else:
                ans+=value
        return ans

