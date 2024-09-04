class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table1 = defaultdict(int)
        table2 = defaultdict(int)

        for num in nums1:
            table1[num]+=1

        for num in nums2:
            table2[num]+=1
        
        output = []
        for k,v in table1.items():
            val2 = table2.get(k)
            if val2 is not None:
                count = min(val2,v)
                output.extend(count*[k])
        return output
