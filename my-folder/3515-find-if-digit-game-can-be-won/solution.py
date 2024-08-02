class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        x = 0
        y = 0
        for num in nums:
            if num>=10:
                x+=num
            else:
                y+=num
        if x>y or y>x:
            return True
        else:
            return False

       


        
