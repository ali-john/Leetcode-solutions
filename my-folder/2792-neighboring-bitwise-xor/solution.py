class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)

        res = 0
        for num in derived:
            res^=num
        return res==0


        # original = [0]
        # original_one = [1]

        # # check for starting 0

        # for i in range(n):
        #     original.append(derived[i]^original[i])
        #     original_one.append(derived[i]^original_one[i])
        
        # valid_0 = (original[0] ==original[-1]) 
        # valid_1 = (original_one[0] == original_one[-1]) 

        # return valid_0 or valid_1


