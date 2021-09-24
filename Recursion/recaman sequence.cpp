/*
Given an integer n. Print first n elements of Recaman’s sequence.
It is basically a function with domain and co-domain as natural numbers and 0. It is recursively defined as below:
Specifically, let a(n) denote the (n+1)-th term. (0 being already there).
The rule says:

a(0) = 0
a(n) = a(n-1) - n      if a(n-1) - n > 0 and is not already present in the sequence
       =  a(n-1) + n    otherwise.

Example 1:

Input: n = 6
Output: 0 1 3 6 2 7
Explaination: Follow the rule and this 
will be the output.
Example 2:

Input: n = 3
Output: 0 1 3
Explaination: If the rule is followed, 
it will produce this output.
Your Task:
You do not need to read input or print anything. Your task is to complete the function recamanSequence() which takes n as the input parameter and returns the sequence.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1 ≤ n ≤ 100
*/

// { Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
// User function Template for C++

class Solution{
public:
  
  void helper(vector<int>& arr,int n,int i)

{

    if(i>n)
      return;

    int x=arr[i-1]-i;
    if (x>0 && !count(arr.begin(),arr.end(),x))
    {
      arr.push_back(x);
      helper(arr,n,i+1);
    }
    else
    {
      x=arr[i-1]+i;
      arr.push_back(x);
      helper(arr,n,i+1);
    }

}

vector<int> recamanSequence(int n){
    // code here
    vector<int> outputs;
    outputs.push_back(0);
    helper(outputs,n,1);
    return outputs;

}

    
};

// { Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        
        Solution ob;
        vector<int> ans = ob.recamanSequence(n);
        for(int i = 0;i < n;i++)
            cout<<ans[i]<<" ";
        cout<<"\n";
    }
    return 0;
}  // } Driver Code Ends
