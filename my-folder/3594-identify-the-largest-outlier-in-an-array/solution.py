class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        #total_sum = sum of (n-2) elements + sum_element + outlier
        #total_sum - sum of (n-2) elements - sum_element = outlier
        # sum_element = sum of (n-2) elements
        # outlier = total_sum - 2 * sum element
        total = sum(nums)
        c = Counter(nums)
        max_outlier = float('-inf')
        for sum_element in c.keys():
            outlier = total - 2*sum_element
            if outlier in c and ( outlier!=sum_element or c[sum_element] > 1):
                max_outlier = max(outlier, max_outlier)
        return max_outlier
