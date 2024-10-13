class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        return self.binarySearch(k)
    
    def binarySearch(self,val):
        left = 0
        right = 5*(val+1)

        while left<=right:
            mid = (left+right)//2
            count = self.countZeros(mid)
            if count<val:
                left = mid+1
            elif count>val:
                right = mid-1
            else:
                return 5
        return 0



    def countZeros(self,num):
        count = 0
        while num:
            num//=5
            count+=num
        return count

