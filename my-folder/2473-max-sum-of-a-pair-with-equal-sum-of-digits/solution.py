class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        table = defaultdict(int)
        max_ans = -1

        for num in nums:
            digit_sum = sum(map(int,str(num)))
            if digit_sum in table:
                prev_num = table[digit_sum]
                max_ans = max(max_ans,prev_num+num)
                table[digit_sum] = max(prev_num,num)
            else:
                table[digit_sum] = num
        return max_ans

