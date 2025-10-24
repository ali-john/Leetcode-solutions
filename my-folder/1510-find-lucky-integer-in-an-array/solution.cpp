class Solution {
public:
    int findLucky(vector<int>& arr) {
        unordered_map<int,int> table;
        for (int num:arr){
            table[num]+=1;
        }
        int lucky = -1;
        for (auto& [key,value]: table){
            if (key == value){
                lucky = max(lucky,key);
            }
        }
        return lucky;
    }
};
