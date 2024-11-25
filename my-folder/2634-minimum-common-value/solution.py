class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        counter1 = Counter(nums1)

        min_common = float('inf')
        for num in nums2:
            if num in counter1:
                min_common = min(min_common,num)
        
        if min_common==float('inf'):
            return -1
        else:
            return min_common
