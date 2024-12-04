class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        words = s.split(' ')
        nums = []
        for char in words:
            if char.isdigit():
                nums.append(int(char))
        
        for i in range(len(nums)-1):
            if nums[i+1]<=nums[i]:
                return False
        return True
