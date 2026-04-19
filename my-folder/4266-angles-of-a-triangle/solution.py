class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        sides = sorted(sides)
        if sides[0] + sides[1] > sides[2]:
            a = sides[0]
            b = sides[1]
            c = sides[2]
            angle1 = degrees( acos( (a**2 + b**2 - c**2) / (2*(a*b)) ))
            angle2 = degrees( acos( (a**2 + c**2 - b**2) / (2*(a*c) )))
            angle3 = degrees( acos( (b**2 + c**2 - a**2) / (2*(b*c)) ))
            return sorted([angle1, angle2, angle3])
            

        else:
            return []
            
