class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start_q = []
        target_q = []

        for i,char in enumerate(start):
            if char!= '_':
                start_q.append((char,i))
        for i,char in enumerate(target):
            if char != "_":
                target_q.append((char,i))
        
        if len(start_q)!= len(target_q): return False
        while start_q:
            start_char, start_index = start_q.pop(0)
            target_char, target_index = target_q.pop(0)

            if ( start_char != target_char or (start_char == 'L' and target_index > start_index) or (start_char == 'R' and target_index < start_index) ):
                return False
        return True




        
