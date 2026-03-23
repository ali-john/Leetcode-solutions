class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        smallest_odd = float('inf')
        odd = False
        for num in nums1:
            if num%2!=0:
                smallest_odd = min(smallest_odd, num)
                odd = True
        if not odd:
            return True
        
        for num in nums1:
            if num%2 == 0 and smallest_odd > num:
                return False
        return True






        # if all(num%2==0 for num in nums1):
        #     return True
        # if all(num%2!=0 for num in nums1):
        #     return True
        
        # smallest_odd = float('inf')
        # for num in nums1:
        #     if num%2 != 0:
        #         smallest_odd = min(smallest_odd, num)
        
        # # try making even
        # possible = True
        # nums1 = sorted(nums1)
        # ans = []
        # for i in range(n):
        #     curr = nums1[i]
        #     if curr%2!=0:
        #         ans.append(curr - smallest_odd)
        #     else:
        #         ans.append(curr)
        # if all( (num%2 ==0 and num>0) for num in ans):
        #     return True
        
        # # try making odd
        # ans = []
        # for i in range(n):
        #     curr = nums1[i]
        #     if curr%2==0:
        #         ans.append(curr - smallest_odd)
        #     else:
        #         ans.append(curr)
        # if all( (num%2 !=0 and num>0) for num in ans):
        #     return True
        # return False
        
        
