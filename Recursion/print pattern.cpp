/* 

PROBLEM STATEMENT:
Print a sequence of numbers starting with N where A[0] = N, without using loop, in which  A[i+1] = A[i] - 5,  
until A[i] > 0. After that A[i+1] = A[i] + 5  repeat it until A[i] = N.

Example 1:

Input: N = 16
Output: 16 11 6 1 -4 1 6 11 16
Explaination: The value decreses until it 
is greater than 0. After that it increases 
and stops when it becomes 16 again.

Example 2:

Input: N = 10
Output: 10 5 0 5 10
Explaination: It follows the same logic as 
per the above example.

Your Task:
You do not need to read input or print anything. Your task is to complete the function pattern() which takes N as input parameters and returns a list 
containing the pattern.

*/

// { Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
// User function Template for C++

class Solution{
public:

    void helper(vector<int> &arr,int N,int i,bool &check)

    {

    if (arr[i]==N && i>0)
    return;

    if (arr[i]>0 && !check)
    {
    int x=arr[i]-5;
    i++;
    arr.push_back(x);
    helper(arr,N,i,check);
    }
    else
    {
    check=true;
    int x=arr[i]+5;
    i++;
    arr.push_back(x);
    helper(arr,N,i,check);

    }


    }

    vector<int> pattern(int N){
        vector<int> outputs;
        outputs.push_back(N);
        bool checker=false;
        helper(outputs,N,0,checker);
        return outputs;
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
        vector<int> ans = ob.pattern(N);
        for(int u: ans)
            cout<<u<<" ";
        cout<<"\n";
    }
    return 0;
}  // } Driver Code Ends
