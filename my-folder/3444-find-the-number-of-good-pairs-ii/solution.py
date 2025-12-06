class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n , m = len(nums1), len(nums2)
        table = defaultdict(int)

        for num in nums2:
            table[num*k]+=1
        
        ans = 0
        for i in range(n):
            num = nums1[i]
            for j in range(1, int(num**0.5)+1):
                if num % j == 0:
                    if j in table:
                        ans+=table[j]
                    if j!= num // j and num // j in table:
                        ans+=table[num//j]
        return ans
