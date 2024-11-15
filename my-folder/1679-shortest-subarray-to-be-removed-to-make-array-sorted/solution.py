class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        left = 0
        right = n-1

        while left<n-1 and (arr[left]<=arr[left+1]):
            left+=1
        
        if left==n-1:
            return 0
        
        while right>0 and arr[right]>=arr[right-1]:
            right-=1
        
        min_length = min(right,n-left-1)
        
        i=0
        j = right
        # remove middle portion
        while i<=left and j<len(arr):
            if arr[i]<=arr[j]:
                min_length = min(j-i-1,min_length)
                i+=1
            else:
                j+=1
        return min_length
