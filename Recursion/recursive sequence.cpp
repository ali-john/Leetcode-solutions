/*
A function f is defined as follows F(N)= (1) +(2*3) + (4*5*6) ... N. Given an integer N the task is to print the F(N)th term.

Example 1:

Input: N = 5
Output: 365527
Explaination: F(5) = 1 + 2*3 + 4*5*6 + 7*8*9*10 
+ 11*12*13*14*15 = 365227.
Your Task:
You do not need to readd input or print anything. Your task is to complete the function sequence() which takes N as input parameter and returns the value of F(N).

Expected Tiime Complexity: O(N2)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 10
*/

// { Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
//User function Template for C++

class Solution{
public:
  
   int summation(int N)
{
int sum=0;
for (int i=1; i<n;i++) 
    sum+=i; 

 return= sum+1;
     
 }

long long sequence(int N)

{

long long fn=0;

for (int i=1; i<=N;i++)
{
int start=summation(i);
long int temp=1;
for (int j=start, k=1;k<=i;k++,j++)
{
temp=temp*j;
}
fn+=temp;

}
return fn;
}
};

// { Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int N;
        cin>>N;
        
        Solution ob;
        cout<<ob.sequence(N)<<endl;
    }
    return 0;
}  // } Driver Code Ends
