class Solution:
    def minimumChairs(self, s: str) -> int:
        waiting_room = 0
        ans = 0
        for char in s:
            if char == "E":
                waiting_room +=1
            else:
                waiting_room-=1
            ans = max(ans, waiting_room)
        return ans

        # for ans in range(51):
        #     # run simulation
        #     temp = ans
        #     possible = True
        #     for char in s:
        #         if char == 'E':
        #             temp-=1
        #         else:
        #             temp+=1
        #         if temp<0: 
        #             possible = False
        #             break
        #     if possible:
        #         return ans



        
