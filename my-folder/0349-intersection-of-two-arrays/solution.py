class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = defaultdict(int)
        for num in nums1:
            table[num]+=1
        output = []
        keys = table.keys()
        for num in nums2:
            if num in keys and num not in output:
                output.append(num)
        return output

