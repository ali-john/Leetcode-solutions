class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        total = Counter(nums1) + Counter(nums2)
        c1 = Counter(nums1)
        c2 = Counter(nums2)

        for val in total.values():
            if val % 2 != 0:
                return -1
        diff = defaultdict()
        for v in total.keys():
            diff[v] = abs(c1[v] - c2[v])
        return sum(diff.values())//4
        

