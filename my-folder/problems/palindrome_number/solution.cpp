#include<bits/stdc++.h>
class Solution {
public:
    
    bool isPalindrome(int x) 
    
    {
        vector <int> hash;
        if (x<0)
            return false;
        else
        {
            if (x>0 && x <=9) // single digits are palindrome
                return true;
            else
            {
                while (x>9)
                {
                    int y = x%10;
                    x = (x-y)/10;
                    hash.push_back(y); // increment count
                }
                hash.push_back(x);
                bool decision = true;
                auto itr1 = hash.begin();
                auto itr2 = hash.rbegin();
                for ( int i=0; i<hash.size()/2; ++i,++itr1,++itr2)
                {
                    if (*itr1!= *itr2)
                        decision = false;
                }
                return decision;
                
                
            }
            
        }
        
    }
};