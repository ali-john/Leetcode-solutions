class Solution:
    def scoreBalance(self, s: str) -> bool:
        n = len(s)
        scores = [0]*n
        for i, char in enumerate(s):
            score = ord(char) - ord('a') + 1
            scores[i] = score
        
        # compute prefix sum
        prefix = [0]*n
        prefix[0] = scores[0]
        for i in range(1,n):
            prefix[i] = scores[i] + prefix[i - 1]
            
        # check possibility:
        for i in range(n):
            left_score = prefix[i]
            right_score = prefix[-1] - left_score
            if left_score == right_score:
                return True
        return False

