class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # sliding window O(n) solution https://youtu.be/RRGvNi-B0RA?si=c2u--GfO40TAtgGH

        abs_diff = list(map(lambda n:abs(n-x),arr))
        min_diff_index = 0
        min_diff = sum_total = sum(abs_diff[0:k])
        for i in range(1,len(arr)-k+1):
            sum_total = abs_diff[i+k-1] + sum_total - abs_diff[i-1]
            if sum_total<min_diff:
                min_diff_index = i
                min_diff = sum_total
        return arr[min_diff_index:min_diff_index+k]


