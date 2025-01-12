class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False
        
        balance = 0
        unlocked = 0
        
        # Left to Right Pass
        for i in range(n):
            if locked[i] == '0':
                unlocked += 1
            elif s[i] == '(':
                balance += 1
            else:
                balance -= 1
            
            if balance < 0:
                if unlocked > 0:
                    unlocked -= 1
                    balance += 1
                else:
                    return False
        
        balance = 0
        unlocked = 0
        
        # Right to Left Pass
        for i in range(n - 1, -1, -1):
            if locked[i] == '0':
                unlocked += 1
            elif s[i] == ')':
                balance += 1
            else:
                balance -= 1
            
            if balance < 0:
                if unlocked > 0:
                    unlocked -= 1
                    balance += 1
                else:
                    return False
        
        return True
