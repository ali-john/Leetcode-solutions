class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = sum(max(a,1) for a in nums1)
        s2 = sum(max(a,1) for a in nums2)
        z1 = nums1.count(0)
        z2 = nums2.count(0)

        if s1>s2 and z2==0: return -1
        if s2>s1 and z1==0: return -1
        return max(s1,s2)



