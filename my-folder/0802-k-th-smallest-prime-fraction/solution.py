class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
    
        right = 1
        left = 0
        ans = [0,1]
        while True:
            mid = (left+right)/2
            count = 0
            ans[0] = 0
            j = 1
            for i in range(n):
                while j<n and arr[i] > mid*arr[j]:
                    j+=1
                count+=n-j
                if j==n:
                    break
                
                if ans[0]*arr[j]<ans[1]*arr[i]: # simply check if the current fraction is greater than what we have before arr[i]/arr[j] > ans[0]/ans[1]
                    ans[0]=arr[i]
                    ans[1] = arr[j]
            
            if count<k: # go to bigger fraction
                left = mid
            elif count>k:
                right = mid
            else:
                return ans



