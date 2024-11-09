class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        
        mid = len(nums)//2
        arr1 = nums[0:mid]
        arr2 = nums[mid:]
        
        ptr1 = 0
        ptr2 = 0

        while ptr1<len(arr1) and ptr2<len(arr2):
            if arr1[ptr1]<arr2[ptr2]:
                arr1[ptr1]*=-1
                arr2[ptr2]*=-1
                ptr1+=1
                ptr2+=1
            else:
                ptr2+=1
        total = 0
        for num in arr1:
            if num>0:
                total+=1
        for num in arr2:
            if num>0:
                total+=1
        return total

