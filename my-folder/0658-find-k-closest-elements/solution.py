class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def search(arr,x):
            left = 0
            right = len(arr)-1

            while left<=right:
                mid = left + (right - left) // 2
                if arr[mid]==x:
                    return mid
                if arr[mid]>x:
                    right = mid-1
                else:
                    left = mid+1
            if left>0:
                return left-1
            else:
                return left
        
        index = search(arr,x)
        windowStart, windowEnd = index, index+1
        output = []
        while k:
            k-=1
            if windowStart>=0 and windowEnd<len(arr):
                distS = abs(x - arr[windowStart])
                distE = abs(x-arr[windowEnd])

                if distS<=distE:
                    output.insert(0,arr[windowStart])
                    windowStart-=1
                else:
                    output.append(arr[windowEnd])
                    windowEnd+=1
            elif windowStart>=0:
                output.insert(0,arr[windowStart])
                windowStart-=1
            elif windowEnd<len(arr):
                output.append(arr[windowEnd])
                windowEnd+=1
        return output

        

        
