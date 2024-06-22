class Solution:
    def reverseBits(self, n: int) -> int:
        n = f'{n:032b}'
        n_list = [i for i in n]
        i=0
        j=31
        while i<j:
            temp = n_list[i]
            n_list[i] = n_list[j]
            n_list[j] = temp
            i+=1
            j-=1
        res = ""
        for x in n_list:
            res+=x
        return int(res,2)
        
"""
Single line solution: return int(f'{n:032b}',2)
"""
        
