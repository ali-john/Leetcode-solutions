class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        if low == 0:
            ans = [0]
        else:
            ans = []
        
        q = [i for i in range(1, 10)]
        while q:
            num = q.pop(0)
            if num > high:
                continue 
            if num >= low:
                ans.append(num)
            last = num%10
            if last > 0:
                q.append(num*10 + last-1)
            if last < 9:
                q.append(num*10 + last + 1)
        
        return ans
            

