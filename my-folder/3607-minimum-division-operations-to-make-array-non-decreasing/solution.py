class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def get_divisor(num):
            max_divisor = 1
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    max_divisor = max(max_divisor, i, num // i)
            return max_divisor

        n = len(nums)
        total = 0

        for i in range(n - 2, -1, -1):
            while nums[i] > nums[i + 1]:
                g = get_divisor(nums[i])
                if g == 1:
                    return -1
                if nums[i] // g > nums[i + 1]:
                    return -1
                nums[i] //= g
                total += 1
                
        return total

