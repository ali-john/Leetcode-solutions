class Solution:
    def balancedString(self, s: str) -> int:
        def check(exceeding,loop_counter)->bool:
            all_check = True
            for excess in exceeding:
                if loop_counter[excess]>= excess_count[excess]:
                    continue
                else:
                    all_check = False
                    break
            return all_check

        n = len(s)
        thr = n//4
        count = Counter(s)
        equal = True
        exceeding = set()
        for key,val in count.items():
            if val>thr:
                exceeding.add(key)
                equal = False
        if equal:
            return 0
        
        excess_count = Counter()
        for word in exceeding:
            excess_count[word] = count[word] - thr
    
        left = 0
        min_val = float("inf")
        loop_counter = Counter()
        for right in range(n):
            loop_counter[s[right]]+=1

            # check if current window has enough count of excess elements then update length    
            while check(exceeding,loop_counter):
                min_val = min(min_val,(right-left)+1)
                loop_counter[s[left]]-=1
                if loop_counter[s[left]]<=0:
                    del loop_counter[s[left]]

                left +=1
        return min_val





