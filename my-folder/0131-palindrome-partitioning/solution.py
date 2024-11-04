class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        curr = []


        def isPalindrome(left,right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True

        def get(i):
            if i>=n:
                ans.append(curr.copy())
                return 
            
            for j in range(i,n):
                if isPalindrome(i,j):
                    curr.append(s[i:j+1])
                    get(j+1)
                    curr.pop()
        get(0)
        return ans
