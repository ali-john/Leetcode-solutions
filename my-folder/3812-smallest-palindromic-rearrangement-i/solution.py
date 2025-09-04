class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        forward = []
        for i in range(n//2):
            forward.append(s[i])
        
        forward = "".join(sorted(forward))
        backward = forward[::-1]
        if n%2 != 0: # odd string
            forward+=s[n//2]
        return forward + backward

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # n = len(s)
        # forward = []
        # for i in range(n//2):
        #     forward.append(s[i])

        # forward = "".join(sorted(forward))
        # backward = forward[::-1]
        # if n%2 !=0:
        #     forward+=s[n//2]

        # return forward + backward
                
        
    
