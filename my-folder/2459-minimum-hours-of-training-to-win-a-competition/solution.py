class Solution:
    def minNumberOfHours(self, e: int, exp: int, energy: List[int], experience: List[int]) -> int:
        n = len(energy)
        ans = 0

        # calculate deficits:
        for i in range(n):
            if e <= energy[i]:
                deficit = (energy[i] - e) + 1
                e+=deficit
                ans+=deficit
            if exp <= experience[i]:
                deficit = (experience[i] - exp) + 1
                exp+=deficit
                ans+=deficit
            
            e-=energy[i]
            exp+=experience[i]
        return ans
            

        
