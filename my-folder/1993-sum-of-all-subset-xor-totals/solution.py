class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        def find_subsets(arr):
            if len(arr)==0:
                return [[]]
            subsets_excluding_first = find_subsets(arr[1:])
            subsets_including_first = [[arr[0]] + subset for subset in subsets_excluding_first]
            return subsets_excluding_first + subsets_including_first
        
        total_subsets = find_subsets(nums)
        for i, subset in enumerate(total_subsets):
            subset_total = 0
            for j in range(len(subset)):
                subset_total^=subset[j]
            total+=subset_total
        return total


                    


