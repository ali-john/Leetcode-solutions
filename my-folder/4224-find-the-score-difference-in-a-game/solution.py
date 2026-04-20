class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        firstActive = True
        secondActive = False
        firstScores = 0
        secondScores = 0

        def find_active_state(index):
            nonlocal firstActive, secondActive
            if nums[index] % 2 != 0:
                firstActive = not firstActive
                secondActive = not secondActive
            if (index + 1) % 6 == 0:
                firstActive = not firstActive
                secondActive = not secondActive
        
        while i < n:
            find_active_state(i)
            if firstActive:
                firstScores+=nums[i]
            else:
                secondScores+=nums[i]
            i+=1
        return firstScores - secondScores


