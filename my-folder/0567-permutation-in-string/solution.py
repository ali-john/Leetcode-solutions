class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:len(s1)])

        if s1_count == window_count:
            return True

        for i in range(len(s1), len(s2)):
            start_char = s2[i - len(s1)]
            end_char = s2[i]

            window_count[end_char] += 1
            window_count[start_char] -= 1

            if window_count[start_char] == 0:
                del window_count[start_char]

            if window_count == s1_count:
                return True

        return False

        
                
            

                

