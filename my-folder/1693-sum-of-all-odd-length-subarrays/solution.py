class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        prefix = []
        n = len(arr)
        for num in arr:
            result+=num
            prefix.append(result)

        # if n%2==0 and n>2: # even length:
        #     result+=prefix[-2]
        # elif n%2==1 and n>2:
        #     result+=prefix[-1]
        
        if len(prefix)>=3:
            j = 2
            while j<len(prefix):
                i = j
                startPtr=-1
                while i<len(prefix):
                    if startPtr>=0:
                        s = prefix[i] - prefix[startPtr]
                    else:
                        s = prefix[i]
    
                    result+=s
                    i+=1
                    startPtr+=1
                j+=2
        return result
