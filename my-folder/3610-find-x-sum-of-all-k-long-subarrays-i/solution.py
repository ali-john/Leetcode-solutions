class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def x_sum(arr):
            table = Counter(arr)
            if len(arr) <=x:
                return sum(arr)
            sorted_list = sorted(table.items(), key = lambda x: (x[1], x[0]), reverse = True)
            keep = set(elem for elem, _ in sorted_list[:x])
    
                # sum only elements in 'keep'
            return sum(num for num in arr if num in keep)

        n = len(nums)
        output = [0]*(n-k+1)
        for i in range(n-k+1):
            sub_arr = nums[i:i+k]
            s = x_sum(sub_arr)
            output[i] = s
        return output






