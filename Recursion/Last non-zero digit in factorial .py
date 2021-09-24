'''
Given a number n, find the last non-zero digit in n!.


Examples:

Input  : n = 5
Output : 2
5! = 5 * 4 * 3 * 2 * 1 = 120
Last non-zero digit in 120 is 2.

Input  : n = 33
Output : 8
Your Task:  
You don't need to read input or print anything. Your task is to complete the function lastNon0Digit() which takes the integer N as input parameters
and returns the last non-zero digit in n!.

'''
#User function Template for python3


class Solution:
  
  def fact(self,N):
    if N == 1:
      return 1
  return N * self.fact(N - 1)

  def lastNon0Digit (self, N):
        pass
        # code here
        x = self.fact(N)
        c = str(x)
        c = c[::-1]
        ans = '0'
        for i in c:
          if i != '0':
            ans = i
            break
        return int(ans)
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ans = ob.lastNon0Digit(N);
        print(ans)




# } Driver Code Ends
