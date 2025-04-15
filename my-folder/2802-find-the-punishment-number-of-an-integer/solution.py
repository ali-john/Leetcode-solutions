class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def is_possible(target, num):
            if not num and target == 0: return True
            if target < 0: return False

            for i in range(len(num)):
                left = num[:i+1]
                right = num[i+1:]
                if is_possible(target - int(left), right):
                    return True
            return False


        ans = 0
        for i in range(1, n+1):
            square = i**2
            if is_possible(i,str(square)):
                ans += square
        return ans


