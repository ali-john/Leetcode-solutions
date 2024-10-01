class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, th: int) -> int:
        n = len(arr)
        
        avg = sum(arr[0:k])
        result = 0
        if avg>=th*k:
            result+=1
        left = 0
        for right in range(k,n):
            avg -= arr[left]
            avg+= arr[right]
            if avg>=th*k:
                result+=1
            left+=1
        return result


