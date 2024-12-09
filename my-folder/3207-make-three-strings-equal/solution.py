class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:

       
        min_len = min(len(s1),len(s2),len(s3))
        equal_upto = -1
        for i in range(min_len):
            if not (s1[i]==s2[i]==s3[i]):
                break
            equal_upto = i
        if equal_upto==-1:
            return -1

        else:
            equal_upto+=1
            op = 0
            op+= (len(s1)-equal_upto)
            op+= (len(s2)-equal_upto)
            op+= (len(s3)-equal_upto)
            return op
            
