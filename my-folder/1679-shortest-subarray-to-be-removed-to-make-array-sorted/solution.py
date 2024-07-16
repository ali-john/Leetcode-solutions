class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)-1

        while l<len(arr)-1 and arr[l]<=arr[l+1]:
            l+=1
        
        if l == len(arr)-1:
            return 0
        while r>0 and arr[r]>=arr[r-1]:
            r-=1
        
        minRemoval = min(len(arr)-l-1,r)
        i=0
        j = r
        while i<=l and j<len(arr):
            if arr[i]<=arr[j]:
                minRemoval = min(j-i-1,minRemoval)
                i+=1
            else:
                j+=1
        return minRemoval

        

        

        






        
