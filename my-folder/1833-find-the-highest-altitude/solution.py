class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = [0]
        i = 0

        for j in range(len(gain)):
            i +=gain[j]
            alt.append(i)
        return max(alt)

