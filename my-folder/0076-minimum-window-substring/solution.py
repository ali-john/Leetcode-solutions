class Solution:
    def check_chars(self,window_counter,t_counter):
        for char, count in t_counter.items():
            if window_counter.get(char,0) < count:
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        window_start = 0
        window_end = 0

        window_counter = Counter()
        t_counter = Counter(t)
        output_strs = []
        min_window = float("inf"), None, None #length, start,end

        while window_end<len(s):
            endChr = s[window_end]
            window_counter[endChr]+=1

            while self.check_chars(window_counter, t_counter) and window_start <= window_end:
                current_window_length = window_end - window_start + 1
                if current_window_length < min_window[0]:
                    min_window = current_window_length, window_start, window_end
                
                startChr = s[window_start]
                window_counter[startChr] -= 1
                if window_counter[startChr] == 0:
                    del window_counter[startChr]
                window_start += 1
            
            window_end+=1
        
        if min_window[1] is None:
            return ""
        else:
            return s[min_window[1]:min_window[2]+1]








        
