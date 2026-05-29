class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        sorted_nums1 = sorted(nums1)
        sorted_nums2 = sorted(nums2)

        remaining = []
        mapping = defaultdict(list)
        i = 0
        for num1 in sorted_nums1:
            if num1 > sorted_nums2[i]:
                mapping[sorted_nums2[i]].append(num1)
                i+=1
            else:
                remaining.append(num1)
        return [mapping[num2].pop() if mapping[num2] else remaining.pop() for num2 in nums2]







