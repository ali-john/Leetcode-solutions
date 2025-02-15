class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0


        def is_possible(target,str_num):
            if not str_num and target ==0:
                return True
            if target<0: return False

            for i in range(len(str_num)):
                left = str_num[:i+1]
                right = str_num[i+1:]
                left_num = int(left)
                if is_possible(target-left_num,right):
                    return True
            return False



        for i in range(1,n+1):
            square = i**2
            if is_possible(i,str(square)):
                ans+=(i**2)
        return ans

