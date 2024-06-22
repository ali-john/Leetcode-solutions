class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = f'{n:032b}'
        count=0
        for e in binary:
            if e=='1':
                count+=1

        return count
        
