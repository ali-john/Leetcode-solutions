class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        output = []
        min_diff = float("inf")
        for i in range(1,len(arr)):
            if abs(arr[i]-arr[i-1])<min_diff:
                min_diff = abs(arr[i]-arr[i-1])
        
        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1])==min_diff:
                sub = [arr[i],arr[i+1]]
                output.append(sub)
        return output
        


        
