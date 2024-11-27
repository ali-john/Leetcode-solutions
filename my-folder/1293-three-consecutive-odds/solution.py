class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        for i in range(len(arr)):
            if arr[i]%2!=0:
                check = True
                for j in range(i+1,i+3):
                    if j<n:
                        if arr[j]%2==0:
                            check = False
                    else:
                        check = False
                        break
                if check:
                    return True
        return False
