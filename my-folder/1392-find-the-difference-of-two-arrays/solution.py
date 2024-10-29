class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []
        l1 = []
        l2 = []

        for i,num in enumerate(nums1):
            if num not in nums2 and num not in l1:
                l1.append(num)
        
        for i,num in enumerate(nums2):
            if num not in nums1 and num not in l2:
                l2.append(num)
        answer.append(l1)
        answer.append(l2)
        return answer

