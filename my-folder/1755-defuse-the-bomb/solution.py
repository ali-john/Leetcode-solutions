class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)

        output = [0]*n
        print(output)
        if k==0:
            return output
        
        if k>0:
            for i in range(n):
                j = (i+1)%n
                curr = 0
                temp = k
                while temp:
                    curr+= code[j]
                    temp-=1
                    j = (j+1) %n
                output[i]=curr
            return output
        else:
            for i in range(n):
                j=i-1%n
                curr = 0
                temp = k
                while temp:
                    curr+=code[j]
                    temp+=1
                    j = (j-1)%n
                output[i] = curr
            return output
                    

