class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        n = len(nums)
        counter = Counter(nums)
        
        def is_possible(val):
            squares = defaultdict(int)
            max_len = float('-inf')
            for i in range(n):
                num = nums[i]
                length = 1
                if num*num in squares:
                    length+=squares[num*num]
                else:
                    temp = num*num
                    while temp in counter:
                        length+=1
                        temp = temp*temp
                    squares[num] = length
                max_len = max(max_len,length)
            if max_len>=val:
                return True
            else:
                return False
            

        left = 0
        right = n
        ans = float('-inf')
        while left<=right:
            mid = (left+right)//2
            if is_possible(mid):
                ans = max(mid,ans)
                left = mid+1
            else:
                right = mid -1

        if ans!=float('-inf'):
            if ans>=2:
                return ans
            else:
                return -1
        else:
            return -1
