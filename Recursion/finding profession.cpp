/*
Consider a special family of Engineers and Doctors with following rules :

Everybody has two children.
First child of an Engineer is an Engineer and second child is a Doctor.
First child of an Doctor is Doctor and second child is an Engineer.
All generations of Doctors and Engineers start with Engineer.
We can represent the situation using below diagram:

                E
           /        \
          E          D
        /   \       /  \
       E     D     D    E
      / \   / \   / \   / \
     E   D D   E  D  E  E  D
Given level and position(pos) of a person in above ancestor tree, find profession of the person.

Example 1:

Input: level = 4, pos = 2
Output: Doctor
Explaination: It is shown in the tree given 
in question.
Example 2:

Input: level = 3, pos = 4
Output: Engineer
Explaination: Already given in the tree in 
question.
Your Task:
You do not need to read input or print anything. Your task is to complete the function profession() which takes level and pos as input parameters and returns 'd' if it 
is a doctor. Otherwise return 'e'. The driver code will output Doctor for 'd' and Engineer for 'e' itself.

Expected Time Complexity: O(log(pos))
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ level ≤ 109
1 ≤ pos ≤ min(109, 2level-1)

*/


// { Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
// User function Template for C++

class Solution{
public:

int countBits(int n)

{

//count ON bits using n & n-1
int on_bits=0;
while(n)
{
n=n&(n-1);
on_bits++;
}
return on_bits;

}

    char profession(int level, int pos){
        // code here
        int x=countBits(pos-1);
        if (x%2==0)
        return 'e';
        else
        return 'd';
    }
};

// { Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int level, pos;
        cin>>level>>pos;
        
        Solution ob;
        if(ob.profession(level, pos) == 'd')
            cout<<"Doctor\n";
        else
            cout<<"Engineer\n";
    }
    return 0;
}  // } Driver Code Ends
