class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        numbers = set()
        for num in nums:
            numbers.add(int(num,2))
        output = None
        def generate(curr):
            if len(curr)==n:
                if int(curr,2) not in numbers:
                    nonlocal output
                    output = curr
                    return
                return
            for digit in ["0","1"]:
                generate(curr+digit)
        generate("")
        return output
