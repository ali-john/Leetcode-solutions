class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        table = defaultdict(int)

        for num in nums:
            table[num]+=1
        
        max_ans = 1
        if table[1]:
            c = table[1] if table[1] % 2 != 0 else table[1] - 1
            max_ans = max(max_ans, c)
        del table[1]
        # check for each value > 1
        for curr_val in table.keys():
            possible = []
            while curr_val <= 10**9:
                next_val = curr_val**2
                cnt = table.get(curr_val, 0)
                next_cnt = table.get(next_val, 0)

                if cnt >= 2 and next_cnt >= 1:
                    possible.append(curr_val)
                else:
                    break
                curr_val = curr_val**2
            if possible:
                max_ans = max(max_ans, len(possible)*2 + 1)
        return max_ans
            

