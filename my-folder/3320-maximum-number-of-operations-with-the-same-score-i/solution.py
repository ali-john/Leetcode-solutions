class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        q = deque()
        for num in  nums:
            q.append(num)
        
        total = 0
        prev = nums[0]+nums[1]

        while len(q)>1:
            first = q.popleft()
            second = q.popleft()
            x = first+second
            if x == prev:
                total+=1
                prev = x
            else:
                break
        return total
        
        
        
