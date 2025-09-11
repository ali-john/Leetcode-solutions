class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        
        return (
            ( sorted(s1[::2]) == sorted(s2[::2]) )
            and 
            ( sorted(s1[1::2]) == sorted(s2[1::2]) )
        )
        
        # n = len(s1)
        # even_list_s1 = []
        # even_list_s2 = []

        # odd_list_s1 = []
        # odd_list_s2 = []
        # for i in range(n):
        #     if i%2==0:
        #         even_list_s1.append(s1[i])
        #         even_list_s2.append(s2[i])
        #     else:
        #         odd_list_s1.append(s1[i])
        #         odd_list_s2.append(s2[i])
        
        # return ( sorted(even_list_s1) == sorted(even_list_s2) ) and (
        #     sorted(odd_list_s1) == sorted(odd_list_s2) )

