class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)

        total_shifts = [0]*n

        for start,end,direction in shifts:
            if direction:
                total_shifts[start]+=1
                if end+1<n: total_shifts[end +1]-=1
            else:
                total_shifts[start]-=1
                if end+1<n: total_shifts[end +1]+=1
        
        for i in range(1,n):
            total_shifts[i] += total_shifts[i-1] 
        
        output = []
        for char,shift in zip(s,total_shifts):
            original_pos = ord(char) - ord('a')
            new_pos = (original_pos + shift) % 26
            new_char = chr(new_pos + ord('a'))
            output.append(new_char)
        return ''.join(output)

