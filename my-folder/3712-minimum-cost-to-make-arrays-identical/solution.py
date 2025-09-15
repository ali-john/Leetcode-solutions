class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        n = len(arr)

        ans1 = 0
        # take diff
        for i in range(n):
            ans1+=abs(arr[i] - brr[i])
        
        # sort and diff
        ans2 = 0
        arr = sorted(arr)
        brr = sorted(brr)
        for i in range(n):
            ans2+=abs(arr[i] - brr[i])
        
        ans = min(ans1, ans2+k)
        return ans
        
        
