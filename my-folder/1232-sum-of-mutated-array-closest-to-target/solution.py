class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        n = len(arr)
        def get_sum(num):
            return sum(num if ele >= num else ele for ele in arr)
        
        low, high = 1, max(arr)
        while low <= high:
            mid = (low+high)//2
            if get_sum(mid) == target:
                return mid
            if get_sum(mid) < target:
                low = mid + 1
            else:
                high = mid - 1
        if abs(target - get_sum(low)) < abs(target - get_sum(high)):
            return low
        return high







