from collections import defaultdict
import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        el1, el2, cnt1, cnt2 = float('inf'), float('inf'), 0, 0

        for num in nums:
            if cnt1==0 and num!=el2:
                cnt1+=1
                el1 = num
            elif cnt2==0 and num!=el1:
                cnt2+=1
                el2 = num
            
            elif num==el1:
                cnt1+=1
            elif num==el2:
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
        output = []
        cnt1, cnt2 = 0, 0 
        for num in nums:
            if num==el1:
                cnt1+=1
            elif num==el2:
                cnt2+=1
        
        if cnt1>math.floor(n/3):
            output.append(el1)
        if cnt2>math.floor(n/3):
            output.append(el2)
        return output


        
