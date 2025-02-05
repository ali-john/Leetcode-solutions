class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        unordered_map<char,int> c1;
        unordered_map<char,int> c2;


        for (char ch:s1)
        {
            c1[ch]+=1;
        }
        for (char ch:s2)
        {
            c2[ch]+=1;
        }
        if (c1!=c2) return false;
        int count = 0;
        for (int i=0; i<min(s1.size(),s2.size()); i++)
        {
            if (s1[i]!=s2[i]) count+=1;
            if (count>2) return false;
        }
        // for (const auto& pair:c1){
        //     cout<<"( "<<pair.first<<", "<<pair.second<<" )"<<endl;
        // }
        return true;


    }
};
