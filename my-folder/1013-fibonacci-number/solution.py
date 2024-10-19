class Solution:
    def fib(self, n: int) -> int:
        table = defaultdict(int)
        table[0]=0
        table[1] = 1
        def ans(num):
            if num<=1:
                return num
            if table[num]!=0:
                return table[num]
            
            total = ans(num-1)+ans(num-2)
            table[num]=total
            return total
        
        return ans(n)

