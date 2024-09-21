class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s = set()
        output = []
        for num in nums:
            if num in s:
                output.append(num)
            
            s.add(num)
        return output
