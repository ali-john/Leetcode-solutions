class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        arr = [-1]*n
        table = {}

        for i in range(n):
            if hours[i]>8:
                arr[i]=1
        
        prev = 0
        total = 0
        for i in range(n):
            prev+=arr[i]
            if prev>0:
                total = max(total,(i+1))
            
            elif prev-1 in table:
                total = max(total,(i - table[prev-1]))
            
            if prev not in table:
                table[prev] = i
        return total
            



        
        






        # # brute force each element
        # max_interval = 0

        # for i in range(n):
        #     curr = new_arr[i]
        #     next_ele = curr
        #     for j in range(i+1,n):
        #         next_ele = next_ele + new_arr[j]
        #         if next_ele>0:
        #             max_interval = max((j-i)+1,max_interval)
        #     if curr>0:
        #         max_interval = max(1,max_interval)
        # return max_interval


