class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        MAX = max(nums)
        limit = (1 << (MAX.bit_length() + 1)) - 1

        def is_palindrome(n):
            bin_n = bin(n)[2:]
            return bin_n == bin_n[::-1]
            
        palindromes = []

        for i in range(1, limit + 1):
            if is_palindrome(i):
                palindromes.append(i)

        #print(palindromes)
        ans = []
        for x in nums:
            i = bisect.bisect_left(palindromes, x)
            best = float('inf')
            if i < len(palindromes): best = min(best, abs(palindromes[i] - x))
            if i > 0: best = min(best, abs(palindromes[i-1] - x))
            ans.append(best)
        return ans

        
        
