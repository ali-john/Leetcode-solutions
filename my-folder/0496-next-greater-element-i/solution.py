class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = {}
        ans = [-1]*len(nums1)
        for indx,num in enumerate(nums2):
            table[num]=table.get(num,0)+indx
        
        for indx,num in enumerate(nums1):
            j = table.get(num)+1
            for i in range(j,len(nums2)):
                if nums2[i]>num:
                    ans[indx]=nums2[i]
                    break
        return ans
        
